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

    mod_req = request_helper.change_request(
        requestId, json_data
    )

    if mod_req:
        return jsonify({'Request updated': mod_req}), 201
    return jsonify(message='Invalid request id or values.'), 400
