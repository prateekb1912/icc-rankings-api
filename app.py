import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False

    app.config['FLASK_DEBUG'] = 1
    app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.SQLALCHEMY_DATABASE_URI

    db = SQLAlchemy()
    db.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)