import unittest
from app import app

class TestJWKS(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_jwks(self):
        response = self.app.get('/jwks')
        self.assertEqual(response.status_code, 200)
        self.assertIn('keys', response.get_json())

if __name__ == '__main__':
    unittest.main()
