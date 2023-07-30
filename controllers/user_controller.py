from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sport_event import SportEvent
from models.user import User
from models.visits import Visit
from app import db

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = User.query.all()
    return render_template("users/index.jinja", users = users)

# @users_blueprint.route ('/users/<id>')
# def show_users (id):
#     user =User.query.get(id)
#     sport_event = SportEvent.query.join(Visit).filter(Visit.user_id == id)
#     return render_template ('users/show.jinja',user = user, sport_event= sport_event)

    
@users_blueprint.route('/users/<int:id>')
def show_users(id):
    user = User.query.get(id)
    sport_events = user.sport_events  # Access sport_events through the new relationship
    
    return render_template('users/show.jinja', user=user, sport_events=sport_events)
