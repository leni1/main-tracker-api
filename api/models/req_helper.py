"""Request Helper class"""
import re

from api.models.request_class import RequestClass


class RequestHelper(object):
    """
    req_db: a list storing requests
    """
    req_db = []

    def check_request(self, req_id, req_name, req_type, req_desc):
        """Method for checking that the request's id, name, type
        and description have valid data types."""
        str_args = [req_name, req_type, req_desc]
        if not isinstance(req_id, int):
            raise ValueError

        for arg in str_args:
            if not isinstance(arg, str):
                raise TypeError

        valid_req_name = re.search(r'^[A-Za-z\s]', req_name)
        valid_req_type = re.search(r'^[A-Za-z\s]', req_type)
        valid_req_desc = re.search(r'^[\w\d!@#$%^&*()-+_/|}{":;\'><~`.,?\s]', req_desc)
        if req_id != 0 and valid_req_name and valid_req_type and valid_req_desc:
            return True
        return False

    def create_request(self, req_id, req_name, req_type, req_desc):
        """Method for creating a request.
        Takes a request's id, name, type and description
        and creates a RequestClass object that is appended to req_db."""
        if self.check_request(req_id, req_name, req_type, req_desc):
            new_req = RequestClass(req_id, req_name, req_type, req_desc)
            self.req_db.append(new_req)
            return vars(new_req)

    def change_request(self, req_id, new_name, new_type, new_desc):
        """Method for modifyng a request.
        Takes a request's id, the new name, type and description
        and updates the RequestClass object with the request id specified."""
        for index, req in enumerate(self.req_db):
            if req_id == req.req_id:
                req = RequestClass(req_id=req_id,
                                   req_name=new_name,
                                   req_type=new_type, req_desc=new_desc)
                self.req_db[index] = req
                return vars(req)
        return False

    def fetch_by_id_request(self, req_id):
        """Method for getting a request by id.
        Takes a request's id and returns a matching
        RequestClass object."""
        if not isinstance(req_id, int):
            raise TypeError
        for req in self.req_db:
            # import pdb; pdb.set_trace()
            if req_id == req.req_id:
                return vars(req)
        return 'Request not found'

    def fetch_all_requests(self):
        """Method for returning all requests in req_db."""
        all_requests = []
        for req in self.req_db:
            all_requests.append(vars(req))
        return all_requests
