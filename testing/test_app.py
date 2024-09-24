import unittest
import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  

class YouTubeDownloaderAPITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        app.config['TESTING'] = True

    def test_get_string(self):
        """Test the /getapi route."""
        response = self.client.get('/getapi')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], "This is a simple string response.")

    def test_index(self):
        """Test the / (index) route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) #Fail build pipeline if a test is wrong >:(

if __name__ == '__main__':
    unittest.main()
