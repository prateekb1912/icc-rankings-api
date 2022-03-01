import sqlalchemy
import os

DEBUG = bool(os.environ.get('FLASK_DEBUG', 1))
CURRENT_API_VERSION = 'v1'

ENABLE_CORS = bool(os.environ.get('ENABLE_CORS', 1))

SQLALCHEMY_TRACK_MODIFICATIONS = False
MAX_CONTENT_LENGTH = 1 * 1000 * 1000

DB_USER = os.environ.get('DB_USER', 'postgres')
DB_HOST = os.environ.get('DB_HOST', 'postgres')
DB_PORT = os.environ.get('POSTGRES_PORT', 5432)
DB_DB = os.environ.get('DB', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')

SQLALCHEMY_DATABASE_URI = sqlalchemy.engine.url.URL.create(
    drivername='postgresql',
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_DB
)

INTERNAL_URL = 9700