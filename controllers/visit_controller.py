from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sport_event import SportEvent
from models.user import User
from models.visits import Visit
from app import db

visits_blueprint = Blueprint("visits", __name__)


@visits_blueprint.route("/visits")
def visits():
    visits = Visit.query.all()
    return render_template("visits/index.jinja", visits = visits)