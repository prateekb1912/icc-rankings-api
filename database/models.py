from sqlalchemy import (
    Column, String, Integer, Enum
)

GenderEnum = Enum('mens', 'womens')
FormatEnum = Enum('tests', 'odis', 't20is')

class Teams():
    rank = Column(Integer)
    team_name = Column(String(20), primary_key=True)
    gender = Column(Enum(GenderEnum), primary_key=True)
    format = Column(Enum(FormatEnum), primary_key=True)
    matches = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)