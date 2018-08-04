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

    new_req = request_handler.create_request(
              request_id, request_name, request_type, request_desc)
    if new_req:
        return jsonify(new_request=vars(new_req)), 201
    return jsonify(message='No request created'), 400

@req.route('/users/requests', methods=['GET'])
def fetch_all_requests():
    all_requests = request_handler.fetch_all_requests()
    return jsonify({'All requests': all_requests}), 200

@req.route('/users/requests/<int:requestId>', methods=['GET'])
def fetch_request_id(requestId):
    result = request_handler.fetch_by_id_request(requestId)
    return jsonify({'Request found': vars(result)}), 200
