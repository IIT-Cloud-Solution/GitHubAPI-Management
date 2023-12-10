import unittest
from app import flask_app1  


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flask_app1.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello Your App is Working!!!', response.data.decode())

    def test_all_commits_missing_parameters(self):
        response = self.app.post('/all_commits', data={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing owner or repo parameters', response.data.decode())

    # This test should fail because the application should not return a 500 error for the index route
    # def test_index_route_fail(self):
    #     response = self.app.get('/')
    #     self.assertEqual(response.status_code, 500, "The index route should not return a 500 error.")

if __name__ == '__main__':
    unittest.main()
