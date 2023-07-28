from app import db

class SportEvent(db.Model):
    __tablename__ = "Sport Event"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sport = db.Column(db.String(64))
    location = db.Column(db.String(64))
    date = db.Column(db.String(64))

    visits = db.relationship('Visit', backref='Sport Event')

    def __repr__(self):
        return f"<Sport Event: {self.id}: {self.name}>"