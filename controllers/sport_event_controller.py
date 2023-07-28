from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sport_event import SportEvent
from models.user import User
from models.visits import Visit

sport_event_blueprint = Blueprint("sport_event", __name__)
