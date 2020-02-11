import unittest
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(self.app is None)

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])
        self.assertFalse(self.app.config['DEVELOPMENT'])
        self.assertFalse(self.app.config['STAGING'])
        self.assertFalse(self.app.config['PRODUCTION'])
        self.assertFalse(self.app.config['HEROKU'])
