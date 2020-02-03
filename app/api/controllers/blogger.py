from app import cache
from flask import current_app
from app.libraries import strip_html as strip

# import json
import requests

timeout = 60 * current_app.config['BLOGGER_DATA_FETCH_PER_DAY'] / 24


@cache.cached(timeout=timeout, key_prefix='getBloggerData')
def getBloggerData():
    url = 'https://www.googleapis.com/blogger/v3/blogs/' + \
        current_app.config['BLOGGER_PAGE_BLOG_ID'] + '/posts'
    params = {
        'key': current_app.config['GOOGLE_API_KEY']
    }

    res = requests.get(url, params=params)
    res_items = res.json().get("items")
    coolarray = []
    for item in res_items:
        theTitle = item["title"]
        theContent = item["content"]
        post = {'title': theTitle, 'content': strip(theContent)}
        coolarray.append(post)
    return coolarray
