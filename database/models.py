from sqlalchemy import (
    Column, Integer, String
)

class TeamRankings():
    position = Column(Integer)
    team = Column(String(15), primary_key=True)
    gender = Column(String(5), primary_key=True)
    format = Column(String(10), primary_key=True)
    matches = Column(Integer)
    points = Column(Integer)
    rating = Column(Integer)

    def __init__(self, position, team, gender, format, matches, points, rating):
        self.position = position
        self.team = team
        self.gender = gender
        self.format = format
        self.matches = matches
        self.points = points
        self.rating = rating

    def serialize(self):
        out = dict()
        out['position'] = self.position
        out['team'] = self.team
        out['gender'] = self.gender
        out['rankingFormat'] = self.format
        out['matchesPlayed'] = self.matches
        out['totalPoints'] = self.points
        out['currentRating'] = self.rating

        return out

    def __repr__(self):
        return f'<Team: {self.team}, Position: {self.position}>'