from app import app
import unittest

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_should_test_hello_message(self):
        result = self.app.get('/hello')
        self.assertEqual('Hello World!', result.data.decode('utf-8'))
