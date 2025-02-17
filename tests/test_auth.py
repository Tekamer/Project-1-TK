import unittest
from app import app

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_token(self):
        response = self.app.post('/auth')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.get_json())

    def test_get_expired_token(self):
        response = self.app.post('/auth?expired=true')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.get_json())

if __name__ == '__main__':
    unittest.main()
