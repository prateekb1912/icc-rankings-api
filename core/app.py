import sqlalchemy

from flask import Flask, jsonify, make_response, g
# from flask_cors import CORS

from core import config
from core.db import db
from api.views import main_api_bp

def register_hooks(app, db):
    @app.errorhandler(404)
    def not_found(e):
        """404 Error handler"""
        return make_response(jsonify({"error": "Not found"}), 404)

    @app.errorhandler(sqlalchemy.exc.IntegrityError)
    @app.errorhandler(sqlalchemy.exc.OperationalError)
    def handle_sqlalchemy_exception(e):
        """Handle SqlAlchemy Errors as specified by the decorators.
        Return HTTP 500.
        """
        g.db.session.rollback()  # This will do the necessary db rollback

        response = jsonify({"error": "Internal Server Error"})
        response.content_type = "application/json"
        response.status_code = 500
        return response

    @app.teardown_request
    def shutdown_session(exception):
        g.db.session.remove()

    @app.before_request
    def create_db_g():
        g.db = db

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False

    app.config["DEBUG"] = config.DEBUG
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)
    register_hooks(app, db)

    app.config['db'] = db

    app.register_blueprint(
        main_api_bp, url_prefix = f'/{config.CURRENT_API_VERSION}/'
    )

    return app