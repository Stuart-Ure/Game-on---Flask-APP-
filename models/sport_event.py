
from app import db
from datetime import date

class SportEvent(db.Model):
    __tablename__ = "Sport Event"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sport = db.Column(db.String(64))
    location = db.Column(db.String(64))
    date = db.Column(db.Date)

    # users = db.relationship('User', secondary='visits')

    def __repr__(self):
        return f"<SportEvent: {self.id}: {self.name}>"