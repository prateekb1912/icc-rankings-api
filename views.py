from flask import Blueprint, jsonify, make_response, request

import config

api_bp = Blueprint('feature_api', __name__)

@api_bp.route('/', methods=['GET'])
def index():
    return "HOME PAGEEE"

@api_bp.route('status', methods=['GET'])
def status():
    print(request)
    response = {"status": True}
    return make_response(jsonify(response), 200)
