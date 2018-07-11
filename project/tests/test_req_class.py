import unittest

from project.api.models.request_class import RequestClass


class TestRequest(unittest.TestCase):
    """Unit Tests for the Request class"""

    def setUp(self):
        self.request_class = RequestClass(1, 'somename', 'sometype', 'somedescription')

    def test_req_class_instance(self):
        self.assertIsInstance(self.request_class, RequestClass, msg='Request class is invalid')
        
    def test_req_attr(self):
        self.assertTrue(hasattr(self.request_class, 'req_id'), msg=AttributeError())
        self.assertTrue(hasattr(self.request_class, 'req_name'), msg=AttributeError())
        self.assertTrue(hasattr(self.request_class, 'req_type'), msg=AttributeError())
        self.assertTrue(hasattr(self.request_class, 'req_desc'), msg=AttributeError())

    def test_req_data_type(self):
        self.assertIsInstance(self.request_class.req_id, int, msg='Wrong request id type')
        self.assertIsInstance(self.request_class.req_name, str, msg='Request name is not a string')
        self.assertIsInstance(self.request_class.req_type,  str, msg='Request type is not a string')
        self.assertIsInstance(self.request_class.req_desc,  str, msg='Request description is not a string')

    def test_req_not_null_field(self):
        self.assertIsNotNone(self.request_class.req_id, msg='The request id is empty')
        self.assertIsNotNone(self.request_class.req_name, msg='The request name is empty')
        self.assertIsNotNone(self.request_class.req_type, msg='The request type is empty')
        self.assertIsNotNone(self.request_class.req_desc, msg='The request description is empty')