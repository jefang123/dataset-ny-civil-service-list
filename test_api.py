import unittest
from unittest.mock import patch
import app
import json

class TestApi(unittest.TestCase):

  # @classmethod
  # def setUpClass(cls):
  #     print("setUpClass")
  
  # @classmethod
  # def tearDownClass(cls):
  #   print("tearDownClass")
  def setUp(self):
    self.app = app.app.test_client()
    self.app.testing = True

  def test_default_endpoint(self):
    response = self.app.get('/')
    data = response.get_data()
    self.assertEqual(response.status_code, 200)
    self.assertEqual(b"Server is running", data)
    self.assertEqual("Server is running", data.decode("utf-8"))

  @patch('basic_client.get_all_datasets', return_value=({"test":"This is a test"}, 200))
  def test_api_endpoint(self, mock_client):
    response = self.app.get('/api')
    data = response.get_data()
    self.assertEqual(data["test"], "This is a test")
    self.assertEqual(response.status_code, 200)

  @patch('basic_client.get_all_datasets', return_value=({"test":"This is a test"}, 500))
  def test_failed_api_endpoint(self, mock_client):
    response = self.app.get('/api')
    data = response.get_data()
    self.assertEqual(response.status_code, 500)

  def test_404(self):
    response = self.app.get('/asdf')
    data = json.loads(response.get_data())
    self.assertEqual(response.status_code, 404)
    self.assertEqual(data["error"], "not found")


  def tearDown(self):
    pass
  #     # reset app.items to initial state
  #     app.items = self.backup_items


if __name__ == "__main__":
    unittest.main()