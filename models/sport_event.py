
from app import db
from datetime import date

class SportEvent(db.Model):
    __tablename__ = "Sport Event"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sport = db.Column(db.String(64))
    location = db.Column(db.String(64))
    date = db.Column(db.Date)

    # visits = db.relationship('Visit', backref='SportEvent', cascade= "all, delete")
    # users = db.relationship('User', secondary='visits', cascade ="all, delete")

    def __repr__(self):
        return f"<SportEvent: {self.id}: {self.name}>"