import unittest
import time
import random
# import json
# from datetime import datetime
from app import create_app
from app.api.utils import sdk


class YoutubeSDKTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        with self.app_context:
            self.controller = sdk.YouTube()

    def tearDown(self):
        self.app_context.pop()

    def test_isValidResource(self):
        _valid_resources = [
            'activities',
            'channels',
            'channelBanners',
            'channelSections',
            'guideCategories',
            'i18nLanguages',
            'i18nRegions',
            'playlists',
            'playlistItems',
            'search results',
            'subscriptions',
            'thumbnails',
            'videos',
            'videoCategories',
            'watermarks'
        ]

        def random_resource(self):
            k = random.randint(0, len(_valid_resources) + 3)
            return _valid_resources[k]

        for resource in _valid_resources:
            self.assertTrue(self.controller.isValidResourceName(resource))

    def test_yt_get_videos(self):
        Options = {'parts': ['id']}  # , 'player', 'snippet'
        videos = self.controller.get('/videos', '/', opts=Options)
        self.assertIsInstance(videos, list)
        # self.assertDictContainsSubset(subset=, dictionary=, msg=)

    def test_yt_response_time(self):
        Options = {'parts': ['id']}  # , 'player', 'snippet'
        ts = {'start': 0, 'stop': 0}
        ts['start'] = time.process_time()
        self.controller.get('videos', '/', opts=Options)
        ts['stop'] = time.process_time()
        self.assertTrue(ts['stop'] - ts['start'] < 4000)
        self.assertFalse(ts['stop'] - ts['start'] > 7000)


if __name__ == '__main__':
    unittest.main()
