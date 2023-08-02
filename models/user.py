from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return f"<User: {self.id}: {self.name}>"
    
    visits= db.relationship("Visit", backref="user")