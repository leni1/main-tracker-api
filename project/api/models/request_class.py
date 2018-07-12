"""Class for the Request"""

class RequestClass(object):
    """
    req_id: integer that identifies a request
    req_name: string value that is the request name
    req_type: string value that is the request type
    req_desc: string value that is the request description"""

    def __init__(self, req_id, req_name, req_type, req_desc):
        if not isinstance(req_id, int):
            raise ValueError
        elif not isinstance(req_name, str):
            raise ValueError
        elif not isinstance(req_name, str):
            raise ValueError
        elif not isinstance(req_desc, str):
            raise ValueError
        else:
            if (req_id != 0 and len(req_name !=0)
                and len(req_type) != 0 and len(req_desc) != 0):
                self.req_id = int(req_id)
                self.req_name = str(req_name)
                self.req_type = str(req_type)
                self.req_desc = str(req_desc)
            else:
                raise "ID, name, type or description is an empty or zero value."
