from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import SportEvent, User, Visit
from app import db

visits_blueprint = Blueprint("visits", __name__)