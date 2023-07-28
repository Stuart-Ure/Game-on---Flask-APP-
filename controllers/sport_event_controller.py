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
