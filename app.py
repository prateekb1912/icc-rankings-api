import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import api_bp

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False

    app.config['FLASK_DEBUG'] = 1
    app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.SQLALCHEMY_DATABASE_URI

    print(config.Config.SQLALCHEMY_DATABASE_URI)

    print("DB TO BE INIT")
    db = SQLAlchemy()
    db.init_app(app)
    print("DB CONFIG")

    app.register_blueprint(api_bp, url_prefix = f'/{config.Config.CURRENT_VERSION_API}')
    print("API BP REGI")

    return app

if __name__ == '__main__':
    print("HOHOYE CREATE APP")
    app = create_app()
    app.run(debug=True)