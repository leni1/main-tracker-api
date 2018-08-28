"""Request Helper module"""
import re

from .request_class import RequestClass


class RequestHelper(object):
    """
    Helper class that handles creating and modifying
    RequestClass objects that represent requests in the system.

    Attributes:
        req_db: List storing requests
        check_request: Method that checks request details
        create_request: Method that creates a request
        change_request: Method that changes a request's details.
        fetch_id_by_request: Method that returns a request matching
        a given id.
        fetch_all_requests: Method that returns all requests present.
    """

    req_db = []

    def check_request(self, req_id, req_name, req_type, req_desc):
        """Checks that the request's id, name, type and description
        have valid data types.

        Makes sure that the request id is an integer, and its name,
        type, and description are strings matching the patterns
        supplied.

        Args:
            req_id: Request id number
            req_name: Request name.
            req_type: Request type.
            req_desc: Request description.

        Returns:
            False: if the request id is 0 and the request name,
            type, and description do not match the string patterns
            supplied.
            True: if the request id is not 0 and the request name,
            type, and description match the string patterns supplied.

        Raises:
            ValueError: The request id was not an integer.
            TypeError: The request name, type or description was not
            a string.
        """

        str_args = [req_name, req_type, req_desc]
        if not isinstance(req_id, int):
            raise ValueError

        for arg in str_args:
            if not isinstance(arg, str):
                raise TypeError

        valid_req_name = re.search(r'^[A-Za-z\s]', req_name)
        valid_req_type = re.search(r'^[A-Za-z\s]', req_type)
        valid_req_desc = re.search(
            r'^[\w\d!@#$%^&*()-+_/|}{":;\'><~`.,?\s]', req_desc)
        if (req_id != 0
           and valid_req_name
           and valid_req_type
           and valid_req_desc):
                return True
        return False

    def create_request(self, req_id, req_name, req_type, req_desc):
        """Creates a request.

        Takes a request's id, name, type and description
        and creates a RequestClass object that is appended to req_db.

        Args:
            req_id: Request id number
            req_name: Request name.
            req_type: Request type.
            req_desc: Request description.

        Returns:
            The created RequestClass object in dictionary form
            For example:

            {'req_id': 1, req_name': 'somename',
            'req_type': 'sometype', 'req_desc': 'somedescription'}
        """

        if self.check_request(req_id, req_name, req_type, req_desc):
            new_req = RequestClass(req_id, req_name, req_type, req_desc)
            self.req_db.append(new_req)
            return vars(new_req)

    def change_req_attr(self, obj, obj_attr, value):
        """Changes an request object's attribute value.

        Takes a request object and changes the RequestClass object
        attribute value if the object has the attribute.

        Args:
            obj: Object whose attribute will be changed
            obj_attr: Object attribute
            value: The value to be assigned to the object's
            attribute.

        Returns:
            obj: The [RequestClass] object with the modified
            attribute.

            False: If the object does not have the attribute passed
            or the attribute (or the value to be assigned to the
            attribute) are not valid.
        """

        valid_value = re.search(r'^[A-Za-z\s]', value)
        valid_attr = re.search(r'^[A-Za-z\s]', obj_attr)
        if (hasattr(obj, obj_attr)
            and valid_value
                and valid_attr):
                setattr(obj, obj_attr, value)
                return obj
        return False

    def change_request(self, req_id, some_dict):
        """Changes a request with matching id.

        Takes a request's id and changes a matching
        RequestClass object if the value of some_dict
        is a dictionary of values.

        Args:
            req_id: Request id number
            some_dict: A dictionary containing the attribute
            to be changed and its value.

        Returns:
            vars(some_obj): The matching RequestClass object
            in dictionary form.

            False: If no matching object is found or an invalid
            value is passed to some_dict

        Raises:
            TypeError: some_dict is not indexed on dictionary
            keys and values.
        """

        for key in some_dict:
            try:
                value = some_dict[key]
            except TypeError:
                raise TypeError
            if key and value:
                for req in self.req_db:
                    if req_id == req.req_id:
                        new_req = self.change_req_attr(
                            req, key, value
                        )
                        return vars(new_req)
        return False

    def fetch_by_id_request(self, req_id):
        """Returns a request with matching id.

        Takes a request's id and returns a matching
        RequestClass object.

        Args:
            req_id: Request id number

        Returns:
            The matching RequestClass object in dictionary form i.e.
            vars(some_obj)
            If no matching object is found, it returns the message
            'Request not found'.

        Raises:
            ValueError: The request id is not an integer.
        """

        if not isinstance(req_id, int):
            raise TypeError
        for req in self.req_db:
            if req_id == req.req_id:
                return vars(req)
        return 'Request not found'

    def fetch_all_requests(self):
        """Returns all requests.

        Takes a request's id and returns a matching
        RequestClass object.

        Args:
            self: RequestHelper class instance

        Returns:
            All RequestClass objects found in req_db in a list of
            dictionaries via vars(some_obj).
        """
        return [vars(req) for req in self.req_db]
