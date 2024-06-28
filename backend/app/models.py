# backend/app/models.py
from . import db

class Soccer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    league = db.Column(db.String(64))
    date_event = db.Column(db.Date)
    home_team = db.Column(db.String(64))
    away_team = db.Column(db.String(64))
    home_score = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
    status = db.Column(db.String(64))
    venue = db.Column(db.String(128))

    def to_dict(self):
        return {
            'league': self.league,
            'date_event': self.date_event.isoformat(),
            'home_team': self.home_team,
            'away_team': self.away_team,
            'home_score': self.home_score,
            'away_score': self.away_score,
            'status': self.status,
            'venue': self.venue
        }

class Basketball(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    league = db.Column(db.String(64))
    date_event = db.Column(db.Date)
    home_team = db.Column(db.String(64))
    away_team = db.Column(db.String(64))
    home_score = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
    status = db.Column(db.String(64))
    venue = db.Column(db.String(128))

    def to_dict(self):
        return {
            'league': self.league,
            'date_event': self.date_event.isoformat(),
            'home_team': self.home_team,
            'away_team': self.away_team,
            'home_score': self.home_score,
            'away_score': self.away_score,
            'status': self.status,
            'venue': self.venue
        }

class Hockey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    league = db.Column(db.String(64))
    date_event = db.Column(db.Date)
    home_team = db.Column(db.String(64))
    away_team = db.Column(db.String(64))
    home_score = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
    status = db.Column(db.String(64))
    venue = db.Column(db.String(128))

    def to_dict(self):
        return {
            'league': self.league,
            'date_event': self.date_event.isoformat(),
            'home_team': self.home_team,
            'away_team': self.away_team,
            'home_score': self.home_score,
            'away_score': self.away_score,
            'status': self.status,
            'venue': self.venue
        }