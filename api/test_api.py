import unittest
import app
import json

class TestApi(unittest.TestCase):

    def setUp(self):
      self.app = app.app.test_client()
      self.app.testing = True

    def test_endpoint(self):
      response = self.app.get('/')
      data = response.get_data()
      self.assertEqual(response.status_code, 200)
      self.assertEqual(b"Server is running", data)
      self.assertEqual("Server is running", data.decode("utf-8"))
    
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