import unittest
from app import app
import werkzeug

# Добавяне на фиктивен атрибут '__version__', ако не съществува
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "2.0.0"  # Можеш да зададеш фиктивна стойност

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello! I am a Flask application", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
