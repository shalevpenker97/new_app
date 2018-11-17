import unittest
import app

class MyTestClass(unittest.TestCase):
    def setUp(self):
        # creates a test client
      #  self.app = app.test_client()
      app.app.config['TESTING']=True
      self.app = app.app.test_client()
        # propagate the exceptions to the test client
      #  self.app.testing = True 

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the response data
        self.assertEqual(result.data, "Hello Wold!!!")
