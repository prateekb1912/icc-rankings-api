import logging
from flask import Blueprint, jsonify, make_response, request

import config

api_bp = Blueprint('feature_api', __name__)
logger = logging.getLogger(f'RANKINGS.{__name__}')

@api_bp.route('status', methods=['GET'])
def status():
    logger.info(request)
    response = {"status": True}
    return make_response(jsonify(response), 200)
