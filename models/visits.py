
from app import db

class Visit(db.Model):
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sport_event_id = db.Column(db.Integer, db.ForeignKey('Sport Event.id'))  # Change the foreign key reference
    comments = db.Column(db.Text())

    # Define the relationship with SportEvent
    sport_event = db.relationship('SportEvent', backref='visits', cascade= "all, delete")  # Add this line

    def __repr__(self):
        return f"<Visit: {self.id}: {self.comments}>"

