import core.config as config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import api_bp

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

app.config['FLASK_DEBUG'] = 1
app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()
db.init_app(app)

app.register_blueprint(api_bp, url_prefix = f'/{config.Config.CURRENT_VERSION_API}')


if __name__ == '__main__':
    app.run(debug=True)