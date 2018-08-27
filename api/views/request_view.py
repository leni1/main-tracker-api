import random
from flask import (
    Blueprint, jsonify, request)

from api.models.req_helper import RequestHelper
request_helper = RequestHelper()

req = Blueprint('req_view', __name__)


@req.route('/users/requests', methods=['POST'])
def create_request():
    json_data = request.get_json()
    request_name = json_data['req_name']
    request_type = json_data['req_type']
    request_desc = json_data['req_desc']
    request_id = random.randint(1, 10000)

    new_req = request_helper.create_request(
              request_id, request_name, request_type, request_desc)
    if new_req:
        return jsonify(new_request=new_req), 201
    return jsonify(message='No request created'), 400


@req.route('/users/requests', methods=['GET'])
def fetch_all_requests():
    all_requests = request_helper.fetch_all_requests()
    return jsonify({'All requests': all_requests}), 200


@req.route('/users/requests/<int:requestId>', methods=['GET'])
def fetch_request_id(requestId):
    result = request_helper.fetch_by_id_request(requestId)
    return jsonify({'Request found': result}), 200


@req.route('/users/requests/<int:requestId>', methods=['PUT'])
def modify_request(requestId):
    json_data = request.get_json()

    for key in json_data.keys():
        if key == 'req_name' and json_data['req_name']:
            new_req_name = json_data['req_name']
            mod_req = request_helper.change_req_name(
                requestId, new_req_name
            )
            if mod_req:
                return jsonify({'Request updated': mod_req}), 201
        elif key == 'req_type' and json_data['req_type']:
            new_req_type = json_data['req_type']
            mod_req = request_helper.change_req_name(
                requestId, new_req_type
            )
            if mod_req:
                return jsonify({'Request updated': mod_req}), 201
        elif key == 'req_desc' and json_data['req_desc']:
            new_req_desc = json_data['req_desc']
            mod_req = request_helper.change_req_desc(
                requestId, new_req_desc
            )
            if mod_req:
                return jsonify({'Request updated': mod_req}), 201
    return jsonify(message='Invalid request id or values.'), 400
