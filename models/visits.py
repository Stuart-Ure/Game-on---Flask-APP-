
from app import db

class Visit(db.Model):
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="cascade"))
    sport_event_id = db.Column(db.Integer, db.ForeignKey('sport_event.id', ondelete="cascade"))  
    comments = db.Column(db.Text())


    def __repr__(self):
        return f"<Visit: {self.id}: {self.comments}>"

