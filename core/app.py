import os
import config as config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.views import api_bp

app = Flask(__name__)

env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.config['JSON_SORT_KEYS'] = False
app.config['FLASK_DEBUG'] = 1
app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()
db.init_app(app)

app.register_blueprint(api_bp, url_prefix = f'/{config.Config.CURRENT_VERSION_API}')


if __name__ == '__main__':
    app.run(debug=True)