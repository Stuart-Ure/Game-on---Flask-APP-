# from app import db

# class Visit(db.Model):
#     __tablename__ = "visits"

#     id = db.Column(db.Integer, primary_key=True) 
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
#     sport_event_id = db.Column(db.Integer, db.ForeignKey('Sport Event.id'))
#     review = db.Column(db.Text())

#     def __repr__(self):
#         return f"<Visit: {self.id}: {self.review}>"
    
    # visits.py

from app import db

class Visit(db.Model):
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    sport_event_id = db.Column(db.Integer, db.ForeignKey('Sport Event.id'))  # Change the foreign key reference
    review = db.Column(db.Text())

    # Define the relationship with SportEvent
    sport_event = db.relationship('SportEvent', backref='visits')  # Add this line

    def __repr__(self):
        return f"<Visit: {self.id}: {self.review}>"
