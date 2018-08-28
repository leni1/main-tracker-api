import inspect
import unittest

from api.models.req_helper import RequestHelper
from api.models.request_class import RequestClass


class TestRequest(unittest.TestCase):
    """Unit Tests for the Request class"""

    def setUp(self):
        self.request_helper = RequestHelper()
        self.req_db = self.request_helper.req_db = []

    def tearDown(self):
        self.req_db = self.request_helper.req_db = []

    def test_req_db_type(self):
        self.assertIsInstance(self.request_helper.req_db, list,
                              msg='Request database is not a list')
        self.assertIsInstance(self.req_db, list,
                              msg='Request database is not a list')

    def test_req_helper_instance(self):
        self.assertIsInstance(self.request_helper, RequestHelper,
                              msg='Request helper class not instantiated')

    def test_req_helper_attributes(self):
        args = ['req_db', 'check_request', 'change_req_attr',
                'change_request', 'fetch_by_id_request',
                'fetch_all_requests']
        for arg in args:
            self.assertTrue(hasattr(self.request_helper, arg),
                            msg='Missing {0} attribute.'.format(arg))

    def test_check_req_method_has_correct_args(self):
        args = ['self', 'req_id', 'req_name', 'req_type', 'req_desc']
        for arg in args:
            self.assertIn(arg, str(inspect.getfullargspec(
                self.request_helper.check_request)),
                msg='Method has no {0} parameter'.format(arg))

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
        args = ['self', 'req_id', 'req_name', 'req_type', 'req_desc']
        for arg in args:
            self.assertIn(arg, str(inspect.getfullargspec(
                self.request_helper.create_request)),
                msg='Method has no {0} parameter'.format(arg))

    def test_create_request_return_object_success(self):
        new_req = self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription')
        self.assertNotEqual(len(self.req_db), 0,
                            msg='No request created')
        for req in self.req_db:
            self.assertIs(vars(req), new_req, msg='No request created.')
            self.assertTrue(hasattr(req, '__dict__'),
                            msg='New request has no __dict__ method.')
            self.assertIsInstance(req, RequestClass,
                                  msg='Invalid RequestClass object')

    def test_change_req_attr_correct_args(self):
        args = ['self', 'obj', 'obj_attr', 'value']
        for arg in args:
            self.assertIn(arg, str(inspect.getfullargspec(
                self.request_helper.change_req_attr)),
                msg='Method has no {0} parameter'.format(arg))

    def test_change_req_attr_success(self):
        self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription')
        for req in self.req_db:
            self.request_helper.change_req_attr(req, 'req_type',
                                                'somefieldvalue')
            self.assertIsInstance(req, object, msg='Invalid object.')
            self.assertTrue(hasattr(req, 'req_type'))
            self.assertEqual(req.req_type, 'somefieldvalue')

    def test_change_req_attr_fail(self):
        samp_obj = self.request_helper.change_req_attr(
            '', 'somefield', 'somefieldvalue'
        )
        self.assertFalse(hasattr(samp_obj, 'somefield'),
                         msg='Invalid objects can be modified.')

    def test_change_request_correct_args(self):
        args = ['self', 'req_id', 'some_dict']
        for arg in args:
            self.assertIn(arg, str(inspect.getfullargspec(
                self.request_helper.change_request)),
                msg='Method has no {0} parameter'.format(arg))

    def test_change_request_fail_type_error(self):
        with self.assertRaises(TypeError):
            self.request_helper.change_request(
                1, 'something'
            )

    def test_change_request_success(self):
        self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription'
        )
        for req in self.req_db:
            mod_req = self.request_helper.change_request(
                1, {'req_type': 'Something new'}
            )
            self.assertIsInstance(mod_req, dict,
                                  msg='Dictionary not returned')

    def test_change_request_fail_empty_field(self):
        self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription'
        )
        for req in self.req_db:
            mod_req = self.request_helper.change_request(
                1, {'': ''}
            )
            self.assertFalse(mod_req, msg='Empty values allowed')

    def test_fetch_req_id_method_has_correct_args(self):
        args = ['self', 'req_id']
        for arg in args:
            self.assertIn(arg, str(inspect.getfullargspec(
                self.request_helper.fetch_by_id_request)),
                msg='Method has no {0} parameter'.format(arg))

    def test_fetch_req_id_non_existent(self):
        self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription')
        self.assertEqual(self.request_helper.fetch_by_id_request(2),
                         'Request not found', msg='Request ID not checked')

    def test_fetch_req_id_invalid(self):
        self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription')
        with self.assertRaises(TypeError):
            self.request_helper.fetch_by_id_request('1')

    def test_fetch_req_id_success(self):
        self.request_helper.create_request(
            1, 'somename', 'sometype', 'somedescription')
        result = self.request_helper.fetch_by_id_request(1)
        self.assertEqual(1, result['req_id'],
                         msg='Request can\'t be fetched by id')

    def test_fetch_all_req_method_has_correct_args(self):
        self.assertIn('self', str(inspect.getfullargspec(
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
