from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        rv = self.app.get('/')
        self.assertIn('Hello', rv.data)

if __name__ == '__main__':
    unittest.main()
