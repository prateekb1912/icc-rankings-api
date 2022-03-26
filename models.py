from app import db
from sqlalchemy.dialects.postgresql import JSON

class Teams(db.Model):
    __tablename__ = 'teams'