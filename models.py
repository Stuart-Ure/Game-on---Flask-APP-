from app import db

class SportEvent(db.Model):
  __tablename__ = "Sport Event"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))
  sport = db.Column(db.String(64))
  Location = db.Column(db.String(64))
  date = db.Column(db.String(64))

  visits = db.relationship('Visit', backref='Sport Event')

  def __repr__(self):
    return f"<Sport Event: {self.id}: {self.name}>"

# #######################################################

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    visits = db.relationship('Visit', backref='user')

    def __repr__(self):
        return f"<User: {self.id}: {self.name}>"

# #######################################################

class Visit(db.Model):
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sport_event_id = db.Column(db.Integer, db.ForeignKey('Sport Event.id'))
    review = db.Column(db.Text())

    def __repr__(self):
        return f"<Visit: {self.id}: {self.review}>"