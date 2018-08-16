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

    def test_modify_req_success(self):
        new_req = self.test_request.post(
            '/users/requests',
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='Failing Test',
                    req_type='Test',
                    description='A failing test')))
        req_id = json.loads(new_req.get_data())['new_request']['req_id']
        response = self.test_request.put(
            '/users/requests/' + str(req_id),
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='New Test Record',
                    req_type='New Test',
                    description='A new failing test'
                )
            ))
        self.assertEqual(response.status_code, 201)

    def test_modify_req_without_name(self):
        new_req = self.test_request.post(
            '/users/requests',
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='Failing Test',
                    req_type='Test',
                    description='A failing test')))
        req_id = json.loads(new_req.get_data())['new_request']['req_id']
        response = self.test_request.put(
            '/users/requests/' + str(req_id),
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='',
                    req_type='New Test',
                    description='A new failing test'
                )
            ))
        self.assertEqual(response.status_code,
                         400, msg='Empty req name allowed')

    def test_modify_req_without_type(self):
        new_req = self.test_request.post(
            '/users/requests',
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='Failing Test',
                    req_type='Test',
                    description='A failing test')))
        req_id = json.loads(new_req.get_data())['new_request']['req_id']
        response = self.test_request.put(
            '/users/requests/' + str(req_id),
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='Failing Test',
                    req_type='',
                    description='A new failing test'
                )
            ))
        self.assertEqual(response.status_code,
                         400, msg='Empty req type allowed')

    def test_modify_req_without_desc(self):
        new_req = self.test_request.post(
            '/users/requests',
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='Failing Test',
                    req_type='Test',
                    description='A failing test')))
        req_id = json.loads(new_req.get_data())['new_request']['req_id']
        response = self.test_request.put(
            '/users/requests/' + str(req_id),
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='New Failing Test',
                    req_type='Test',
                    description=''
                )
            ))
        self.assertEqual(response.status_code,
                         400, msg='Empty req description allowed')
