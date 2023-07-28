from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import SportEvent, User, Visit
from app import db

users_blueprint = Blueprint("users", __name__)