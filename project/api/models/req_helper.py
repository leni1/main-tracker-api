"""Request Helper class"""
from project.api.models.request_class import RequestClass


class RequestHelper():
    """
    req_db: a list storing requests
    """
    req_db = []

    def check_request(self, req_id, req_name, req_type, req_desc):
        """Method for checking that the request's id, name, type
        and description have valid data types."""
        str_args = [req_name, req_type, req_desc]
        if not isinstance(req_id, int):
            raise TypeError
        for arg in str_args:
            if not isinstance(arg, str):
                raise TypeError

        if (req_id != 0 and len(req_name) != 0
           and len(req_type) != 0 and len(req_desc) != 0):
            return True
        else:
            return 'ID, name, type and description cannot be 0 or empty'

    def create_request(self, req_id, req_name, req_type, req_desc):
        """Method for creating a request.
        Takes a request's id, name, type and description
        and creates a RequestClass object that is appended to req_db."""
        if self.check_request(req_id, req_name, req_type, req_desc):
            new_req = RequestClass(req_id=req_id, req_name=req_name,
                                   req_type=req_type, req_desc=req_desc)
            self.req_db.append(new_req)
            return self.req_db
        else:
            return 'Unable to add request'

    def change_request(self, req_id, new_name, new_type, new_desc):
        """Method for modifyng a request.
        Takes a request's id, the new name, type and description
        and updates the RequestClass object with the request id specified."""
        if self.check_request(req_id, new_name, new_type, new_desc):
            for index, req in enumerate(self.req_db):
                if req_id == req.req_id:
                    req = RequestClass(req_id=req_id,
                                       req_name=new_name,
                                       req_type=new_type, req_desc=new_desc)
                self.req_db[index] = req
            return self.req_db

    def fetch_by_id_request(self, req_id):
        """Method for getting a request by id.
        Takes a request's id and returns a matching
        RequestClass object."""
        if not isinstance(req_id, int):
            raise TypeError
        for req in self.req_db:
            if req_id == req.req_id:
                return req
            else:
                return 'Request not found'

    def fetch_all_requests(self):
        """Method for returning all requests in req_db."""
        return self.req_db
