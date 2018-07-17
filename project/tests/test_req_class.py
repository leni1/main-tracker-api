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
