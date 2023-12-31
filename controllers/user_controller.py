from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sport_event import SportEvent
from models.user import User
from models.visits import Visit
from app import db

users_blueprint = Blueprint("users", __name__)


users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = User.query.all()
    return render_template("users/index.jinja", users = users)

# search by instance of user

@users_blueprint.route('/users/<int:id>')
def show_users(id):
    user = User.query.get(id)
    sport_events = SportEvent.query.join(Visit).filter(Visit.user_id == user.id)
    all_sport_events = SportEvent.query.all() 
    return render_template('users/show.jinja', user=user, sport_events=sport_events,  all_sport_events=all_sport_events)


# add route to state user has attended an event. 
@users_blueprint.route('/users/<int:id>/add_attended_event', methods=['POST'])
def add_attended_event(id):
    user = User.query.get(id)
    event_id = request.form.get('event_id')
    
    if event_id:
        visit = Visit(user_id=user.id, sport_event_id=event_id)
        db.session.add(visit)
        db.session.commit()
    
    return redirect(f"/users/{user.id}")


@users_blueprint.route('/users/<int:id>', methods=['GET', 'POST'])
def show(id):
    user = User.query.get(id)
    all_sport_events = SportEvent.query.all()  

    if request.method == 'POST':
        event_id = request.form.get('event_id')
        comment = request.form.get('comment')

        if event_id:
            visit = Visit.query.filter_by(user_id=user.id, sport_event_id=event_id).first()
            if visit:
                visit.comments = comment
                db.session.commit()

    return render_template("users/show.jinja", user=user, all_sport_events=all_sport_events)

#add a new user

@users_blueprint.route("/users", methods=['POST'])
def create_user():
    name = request.form.get('name')
    
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

    #delete user

@users_blueprint.route('/users/<int:id>/delete', methods = ['POST'])
def delete_user(id):
    delete_user = User.query.get(id)
    db.session.delete(delete_user)
    db.session.commit()
    return redirect("/users")





