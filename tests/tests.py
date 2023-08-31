import unittest
from todo import *

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"This is a message from the Flask app!", response.data)

if __name__ == '__main__':
    unittest.main()