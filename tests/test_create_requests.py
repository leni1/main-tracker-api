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

    def test_create_request(self):
        new_req = self.test_request.post('/users/requests',
                                         content_type='application/json',
                                         data=json.dumps(
                                             dict(name='Failing Test',
                                                  req_type='Test',
                                                  description='A failing test')
                                                  ))
        self.assertEqual(new_req.status_code, 201)

    def test_create_request_without_name(self):
        new_req = self.test_request.post('/users/requests',
                                         content_type='application/json',
                                         data=json.dumps(
                                             dict(name='',
                                                  req_type='Test',
                                                  description='A failing test')
                                                  ))
        self.assertEqual(new_req.status_code,
                         400, msg='Empty req name allowed')

    def test_create_request_without_type(self):
        new_req = self.test_request.post('/users/requests',
                                         content_type='application/json',
                                         data=json.dumps(
                                             dict(name='Failing Test',
                                                  req_type='',
                                                  description='A failing test')
                                                  ))
        self.assertEqual(new_req.status_code,
                         400, msg='Empty req type allowed')

    def test_create_request_without_desc(self):
        new_req = self.test_request.post('/users/requests',
                                         content_type='application/json',
                                         data=json.dumps(
                                             dict(name='Failing Test',
                                                  req_type='Test',
                                                  description='')
                                                  ))
        self.assertEqual(new_req.status_code,
                         400, msg='Empty req description allowed')
