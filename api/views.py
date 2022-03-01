from flask import Blueprint, request, make_response, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy

main_api_bp = Blueprint('team_rankings_api', __name__)

@main_api_bp.route('status')
def status_service():
    data = {'status': True}
    return make_response(jsonify(data), 200)