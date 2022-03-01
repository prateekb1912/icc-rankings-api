from sqlalchemy import (
    Column, Boolean
)

from sqlalchemy import (
    PrimaryKeyConstraint, Column, Integer, String, Index, BigInteger, ForeignKey, Enum
)

class TeamRankings():
    position = Column(Integer)
    team = Column(String(15), primary_key=True)
    gender = Column(String(5), primary_key=True)
    format = Column(String(10), primary_key=True)
    matches = Column(Integer)
    points = Column(Integer)
    rating = Column(Integer)

    def serialize(self):
        out = dict()
        out['position'] = self.position
        out['team'] = self.team
        out['gender'] = self.gender
        out['format'] = self.format
        out['matches'] = self.matches
        out['points'] = self.points
        out['rating'] = self.rating

        return out