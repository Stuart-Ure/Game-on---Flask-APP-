from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sport_event import SportEvent
from models.user import User
from models.visits import Visit

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


@sport_event_blueprint.route("/sportevents/<int:id>")
def show(id):
    sport_event = SportEvent.query.get(id)
    if sport_event is None:
        return render_template("errors/404.jinja"), 404

    return render_template("sportevents/show.jinja", sport_event=sport_event)