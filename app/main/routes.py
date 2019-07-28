from app.main import bp
from app.main.youtube import getYouTubeData, getAllYouTubeVideosByPlaylistId
from app.main.facebook import getFacebookPosts
from app.main.blogger import getBloggerData
from flask import current_app, render_template, jsonify, abort

@bp.route('/')
@bp.route('/index')
def index():
    return render_template(
        'index.html', 
        videos=getYouTubeData(), 
        channelID=current_app.config['YOUTUBE_CHANNEL_ID'],
        fbAppId=current_app.config['FACEBOOK_APP_ID'],
        fbAppVer=current_app.config['FACEBOOK_API_VERSION']
    )

@bp.route('/fb-posts')
def fbPosts():
    posts = getFacebookPosts()
    return jsonify({'posts': posts})
 
@bp.route('/yt-posts')
def ytPosts():
    posts = getYouTubeData()
    return jsonify({'posts': posts})
    
@bp.route('/blog-posts')
def blogPosts():
	posts = getBloggerData()	
	return jsonify({'posts': posts})
