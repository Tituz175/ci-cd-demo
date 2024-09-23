import unittest
from main import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.get('/add?a=10&b=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 15)

    def test_subtract(self):
        response = self.app.get('/subtract?a=10&b=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 5)

if __name__ == "__main__":
    unittest.main()
