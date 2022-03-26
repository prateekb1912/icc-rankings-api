import os
import sqlalchemy

from dotenv import load_dotenv
from sqlalchemy.engine import create_engine
from sqlalchemy_utils import database_exists, create_database


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class Config(object):
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")
    CURRENT_VERSION_API = 'v1'

    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_DB = os.getenv('DB_DB')

    SQLALCHEMY_DATABASE_URI = sqlalchemy.engine.url.URL.create(
        drivername='postgresql',
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DB
    )

    db_engine = create_engine(SQLALCHEMY_DATABASE_URI)

    if not database_exists(db_engine.url):
        create_database(db_engine.url)

class ProductionConfig(Config):
    pass

class StagingConfig(Config):
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True