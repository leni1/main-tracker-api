import unittest

from api.models.request_class import RequestClass


class TestRequest(unittest.TestCase):
    """Unit Tests for the Request class"""

    def test_req_class_instance(self):
        self.request_class = RequestClass(1, 'somename',
                                          'sometype', 'somedescription')
        self.assertIsInstance(self.request_class, RequestClass,
                              msg='Request class is invalid')

    def test_req_attr(self):
        args = ['req_id', 'req_name', 'req_type', 'req_desc']
        self.request_class = RequestClass(1, 'somename',
                                          'sometype', 'somedescription')
        for arg in args:
            self.assertTrue(hasattr(self.request_class, arg),
                            msg=AttributeError)
