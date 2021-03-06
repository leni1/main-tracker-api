"""Request class module"""


class RequestClass(object):
    """
    Request class object

    The class that represents requests in the system.

    Attributes:
        req_id: integer that identifies a request
        req_name: string value that is the request name
        req_type: string value that is the request type
        req_desc: string value that is the request description"""

    def __init__(self, req_id, req_name, req_type, req_desc):
            self.req_id = int(req_id)
            self.req_name = str(req_name)
            self.req_type = str(req_type)
            self.req_desc = str(req_desc)
