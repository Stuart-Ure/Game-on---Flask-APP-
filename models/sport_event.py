
from app import db
from datetime import date

class SportEvent(db.Model):
    __tablename__ = "sport_event"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sport = db.Column(db.String(64))
    location = db.Column(db.String(64))
    date = db.Column(db.Date)
    
    visits= db.relationship("Visit", backref="sport_event")

    def __repr__(self):
        return f"<SportEvent: {self.id}: {self.name}>"