from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, DateTime, String, Enum, Integer
from sqlalchemy.sql import func

import re

class IDSModelBase(object):
    """
    custom base class model.
    """

    @declared_attr
    def __tablename__(cls):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    created = Column(DateTime, server_default=func.now(),
                     comment="The creation time\
                              of the entry")
    modified = Column(DateTime, server_default=func.now(),
                      comment="The last modification\
                               time of the entry")
    accessed = Column(DateTime, server_default=func.now(),
                      comment="The last time the entry\
                               was involved in an IDS\
                               event or scan event")


Base = declarative_base(cls=IDSModelBase)
metadata = Base.metadata


class Teams(Base):
    rank = Column(Integer)
    team_name = Column(String(20), primary_key=True)
    gender = Column(Enum('mens', 'womens', name = 'gender'), primary_key=True)
    format = Column(Enum('tests', 'odis', 't20is', name = 'format'), primary_key=True)
    matches = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)