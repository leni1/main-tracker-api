import unittest

from project.api.models.request_class import RequestClass


class TestRequest(unittest.TestCase):
    """Unit Tests for the Request class"""

    def test_req_class_instance(self):
        self.request_class = RequestClass(1, 'somename', 'sometype', 'somedescription')
        self.assertIsInstance(self.request_class, RequestClass, msg='Request class is invalid')

    def test_req_attr(self):
        self.request_class = RequestClass(1, 'somename', 'sometype', 'somedescription')
        self.assertTrue(hasattr(self.request_class, 'req_id'), msg=AttributeError)
        self.assertTrue(hasattr(self.request_class, 'req_name'), msg=AttributeError)
        self.assertTrue(hasattr(self.request_class, 'req_type'), msg=AttributeError)
        self.assertTrue(hasattr(self.request_class, 'req_desc'), msg=AttributeError)

    def test_req_data_type(self):
        self.request_class = RequestClass(1, 'somename', 'sometype', 'somedescription')
        self.assertIsInstance(self.request_class.req_id, int, msg=ValueError)
        self.assertIsInstance(self.request_class.req_name, str, msg='Request name is not a string')
        self.assertIsInstance(self.request_class.req_type,  str, msg='Request type is not a string')
        self.assertIsInstance(self.request_class.req_desc,  str, msg='Request description is not a string')

    def test_req_not_null_field(self):
        self.request_class = RequestClass(0, '', '', '')
        self.assertEqual(self.request_class.req_id, 0, msg='ID cannot be zero')
        self.assertEqual(len(self.request_class.req_name), 0, msg='Name is empty')
        self.assertEqual(len(self.request_class.req_type), 0, msg='Type is empty')
        self.assertEqual(len(self.request_class.req_desc), 0, msg='Description is empty')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.request_class = RequestClass('', 1, 1, 1)
            self.request_class = RequestClass(5, 'something', 1, 1)
