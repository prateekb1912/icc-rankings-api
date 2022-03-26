from flask import Blueprint, jsonify, make_response, request

import core.config as config

api_bp = Blueprint('feature_api', __name__)

@api_bp.route('/', methods=['GET'])
def index():
    return "HOME PAGE"

@api_bp.route('status', methods=['GET'])
def status():
    response = {"status": True}
    return make_response(jsonify(response), 200)