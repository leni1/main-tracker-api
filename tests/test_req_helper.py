import inspect
import unittest

from api.models.req_helper import RequestHelper
from api.models.request_class import RequestClass


class TestRequest(unittest.TestCase):
    """Unit Tests for the Request class"""

    def setUp(self):
        self.request_helper = RequestHelper()
        self.req_db = []

    def tearDown(self):
        self.req_db

    def test_req_db_type(self):
        self.assertIsInstance(self.req_db, list,
                              msg='Request database is not a list')

    def test_req_helper_instance(self):
        self.assertIsInstance(self.request_helper, RequestHelper,
                              msg='Request helper class not instantiated')

    def test_req_helper_methods(self):
        self.assertTrue(hasattr(self.request_helper, 'req_db'),
                        msg='Missing request database')
        self.assertTrue(hasattr(self.request_helper, 'check_request'),
                        msg='Missing check_request method')
        self.assertTrue(hasattr(self.request_helper, 'create_request'),
                        msg='Missing create_request method')
        self.assertTrue(hasattr(self.request_helper, 'change_request'),
                        msg='Missing change_request method')
        self.assertTrue(hasattr(self.request_helper, 'fetch_all_requests'),
                        msg='Missing fetch_all_requests method')
        self.assertTrue(hasattr(self.request_helper, 'fetch_by_id_request'),
                        msg='Missing fetch_by_id_method')

    def test_check_req_method_has_correct_args(self):
        self.assertIn('self', str(
                      inspect.getfullargspec(
                          self.request_helper.check_request)),
                      msg='Method has no self parameter')
        self.assertIn('req_id', str(
                      inspect.getfullargspec(
                          self.request_helper.check_request)),
                      msg='Method has no req_id parameter')
        self.assertIn('req_name', str(
                      inspect.getfullargspec(
                          self.request_helper.check_request)),
                      msg='Method has no req_name parameter')
        self.assertIn('req_type', str(
            inspect.getfullargspec(self.request_helper.check_request)),
            msg='Method has no req_type parameter')
        self.assertIn('req_desc', str(
            inspect.getfullargspec(self.request_helper.check_request)),
            msg='Method has no req_desc parameter')

    def test_check_req_method_raise_error(self):
        with self.assertRaises(ValueError):
            self.request_helper.check_request('', 'somename',
                                              'sometype', 'somedescription')
        with self.assertRaises(TypeError):
            self.request_helper.check_request(1, 1,
                                              'sometype', 'somedescription')
        with self.assertRaises(TypeError):
            self.request_helper.check_request(1, 'somename',
                                              1, 'somedescription')
        with self.assertRaises(TypeError):
            self.request_helper.check_request(1, 'somename',
                                              'sometype', 1)

    def test_check_req_method_null_values(self):
        invalid_req = self.request_helper.check_request(0, '', '', '')
        self.assertEqual(invalid_req, False,
                         msg='Method accepts zero or empty values')

    def test_check_req_method_success(self):
        valid_req = self.request_helper.check_request(1, 'somename',
                                                      'sometype', 'somedesc')
        self.assertTrue(valid_req, msg='Parameters not checked')

    def test_create_req_method_has_correct_args(self):
        self.assertIn('self', str(
                      inspect.getfullargspec(
                          self.request_helper.create_request)),
                      msg='Method has no self parameter')
        self.assertIn('req_id', str(
                      inspect.getfullargspec(
                          self.request_helper.create_request)),
                      msg='Method has no req_id parameter')
        self.assertIn('req_name', str(
                      inspect.getfullargspec(
                          self.request_helper.create_request)),
                      msg='Method has no req_name parameter')
        self.assertIn('req_type', str(
                      inspect.getfullargspec(
                          self.request_helper.create_request)),
                      msg='Method has no req_type parameter')
        self.assertIn('req_desc', str(
            inspect.getfullargspec(self.request_helper.create_request)),
            msg='Method has no req_desc parameter')

    def test_create_request_return_object_success(self):
        new_req = self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription')
        for req in self.req_db:
            self.assertIs(vars(req), new_req, msg='No request created.')
            self.assertTrue(hasattr(req, '__dict__'),
                            msg='New request has no __dict__ method.')
            self.assertIsInstance(req, RequestClass,
                                  msg='Invalid RequestClass object')

    def test_change_req_method_has_correct_args(self):
        self.assertIn('self', str(
                      inspect.getfullargspec(
                          self.request_helper.change_request)),
                      msg='Method has no self parameter')
        self.assertIn('req_id', str(
                      inspect.getfullargspec(
                          self.request_helper.change_request)),
                      msg='Method has no req_id parameter')
        self.assertIn('new_name', str(
                      inspect.getfullargspec(
                          self.request_helper.change_request)),
                      msg='Method has no new_name parameter')
        self.assertIn('new_type', str(
                      inspect.getfullargspec(
                          self.request_helper.change_request)),
                      msg='Method has no new_type parameter')
        self.assertIn('new_desc', str(
                      inspect.getfullargspec(
                          self.request_helper.change_request)),
                      msg='Method has no new_desc parameter')

    def test_change_req_method_success(self):
        self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription')
        for req in self.req_db:
            old_req_name = req.req_name
            old_req_type = req.req_type
            old_req_desc = req.req_desc
            mod_req = self.request_helper.change_request(
                        1, 'newname', 'newtype', 'newdescription')
            self.assertNotEqual(old_req_name, req.req_name,
                                msg='Request name not updated.')
            self.assertNotEqual(old_req_type, req.req_type,
                                msg='Request type not updated.')
            self.assertNotEqual(old_req_desc, req.req_desc,
                                msg='Request description not updated.')
            self.assertIs(mod_req, req, msg='Request not changed')

    def test_fetch_req_id_method_has_correct_args(self):
        self.assertIn('self', str(
                      inspect.getfullargspec(
                          self.request_helper.fetch_by_id_request)),
                      msg='Method has no self parameter')
        self.assertIn('req_id', str(
                      inspect.getfullargspec(
                          self.request_helper.fetch_by_id_request)),
                      msg='Method has no req_id parameter')

    def test_fetch_req_id_invalid(self):
        self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription')
        self.assertEqual(self.request_helper.fetch_by_id_request(2),
                         'Request not found', msg='Request ID not checked')

    def test_fetch_req_id_success(self):
        self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription')
        result = self.request_helper.fetch_by_id_request(1)
        self.assertEqual(1, result['req_id'],
                         msg='Request can\'t be fetched by id')

    def test_fetch_all_req_method_has_correct_args(self):
        self.assertIn('self', str(
                      inspect.getfullargspec(
                          self.request_helper.fetch_all_requests)),
                      msg='Method has no self parameter')

    def test_fetch_all_req_method_success(self):
        self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription')
        result = self.request_helper.fetch_all_requests()
        self.assertIsInstance(result, list,
                              msg='Fetch all method not returning list db')
        self.assertNotEqual(len(result), 0,
                            msg='No Request objects in the db to retrieve.')
