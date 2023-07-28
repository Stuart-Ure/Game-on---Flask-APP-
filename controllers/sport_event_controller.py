from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import User, SportEvent, Visit

sport_event_blueprint = Blueprint("sport_event", __name__)
