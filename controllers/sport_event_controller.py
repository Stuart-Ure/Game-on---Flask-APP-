from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sport_event import SportEvent
from models.user import User
from models.visits import Visit
from app import db

sport_event_blueprint = Blueprint("sport_event", __name__)

@sport_event_blueprint.route("/sportevents")
def sport_events():
    sport_events = SportEvent.query.all()
    return render_template("sportevents/index.jinja", sport_events=sport_events)


# @sport_event_blueprint.route("/sportevents/<int:id>")
# def show(id):
#     sport_event = SportEvent.query.get(id)
#     users = User.query.join(Visit).filter(Visit.sport_event_id ==id)
#     return render_template("sportevents/show.jinja", sport_event = sport_event, users =users)

#HERE I AM ALLOWING THE SPORT EVENT INSTANCE TO BE SEARCHED BY ID FROM THE DATABASE

@sport_event_blueprint.route("/sportevents/<int:id>")
def show(id):
    sport_event = SportEvent.query.get(id)
    # if sport_event is None:
    #     return render_template("errors/404.jinja"), 404

    return render_template("sportevents/show.jinja", sport_event=sport_event)



@sport_event_blueprint.route("/sportevents", methods=['POST'])
def create_sport_event():
    name = request.form.get('name')
    sport = request.form.get('sport')
    location = request.form.get('location')
    date = request.form.get('date')

    #add new event

    new_sport_event = SportEvent(name=name, sport=sport, location=location, date=date)
    db.session.add(new_sport_event)
    db.session.commit()

    return redirect('/sportevents')

    #delete event

@sport_event_blueprint.route("/sportevents/<int:id>/delete", methods=["POST"])
def delete_sport_event(id):
    sport_event = SportEvent.query.get(id)
    db.session.delete(sport_event)
    db.session.commit()
    return redirect("/sportevents")

