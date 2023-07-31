from app import db
from models.sport_event import SportEvent
from models.user import User
from models.visits import Visit


import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    SportEvent.query.delete()
    User.query.delete()
    user1= User(name="Stuart")
    user2= User(name ="Scott")
    user3= User(name="Liam")
    event1= SportEvent(name="Wimbledon Final",sport="Tennis", location="London", date="8th,July,2023")
    event2= SportEvent(name="Ashes 5th test",sport="Cricket", location="Melbourne", date="26th, December,2022")

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
 
    db.session.add(event1)
    db.session.add(event2)
    db.session.commit()

