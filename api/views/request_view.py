import random
from flask import (
    Blueprint, jsonify, request)

from api.models.req_helper import RequestHelper
request_handler = RequestHelper()

req = Blueprint('req_view', __name__)

@req.route('/users/requests', methods=['POST'])
def create_request():
    json_data = request.get_json()
    request_name = json_data['name']
    request_type = json_data['req_type']
    request_desc = json_data['description']
    request_id = random.randint(1, 10000)

    new_req = request_handler.create_request(request_id, request_name, request_type, request_desc)
    if new_req:
        return jsonify(new_request=vars(new_req)), 201
    return jsonify(message='No request created'), 400
