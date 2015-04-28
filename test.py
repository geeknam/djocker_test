import flaskr
import unittest

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flaskr.app.test_client()

    def test_homepage(self):
        rv = self.app.get('/')
        assert 'Hello' in rv.data