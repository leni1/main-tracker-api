import json
import unittest
from api import create_app
from api.models.req_helper import RequestHelper


class MaintenanceViews(unittest.TestCase):
    """Tests the enpoints contains in request_views.py"""

    def setUp(self):
        self.test_app = create_app({'TESTING': True})
        self.test_request = self.test_app.test_client()
        with self.test_app.app_context():
            self.req_db = RequestHelper.req_db

    def tearDown(self):
        self.req_db

    def test_fetch_all_requests(self):
        self.test_request.post(
            '/users/requests',
            content_type='application/json',
            data=json.dumps(
                dict(
                    req_name='Failing Test',
                    req_type='Test',
                    req_desc='A failing test')))
        response = self.test_request.get('/users/requests',
                                         content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_request_id(self):
        new_req = self.test_request.post(
            '/users/requests',
            content_type='application/json',
            data=json.dumps(
                dict(
                    req_name='Failing Test',
                    req_type='Test',
                    req_desc='A failing test')))
        req_id = json.loads(new_req.get_data())['new_request']['req_id']
        response = self.test_request.get(
            '/users/requests/' + str(req_id),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
