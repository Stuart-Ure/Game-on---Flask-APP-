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
    all_sport_events = SportEvent.query.all() 
    return render_template('users/show.jinja', user=user, sport_events=sport_events,  all_sport_events=all_sport_events)

@users_blueprint.route('/users/<int:id>/add_attended_event', methods=['POST'])
def add_attended_event(id):
    user = User.query.get(id)
    event_id = request.form.get('event_id')
    
    if event_id:
        # Update the database to mark the event as attended by the user
        visit = Visit(user_id=user.id, sport_event_id=event_id)
        db.session.add(visit)
        db.session.commit()
    
    return redirect(f"/users/{user.id}")

