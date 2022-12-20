from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.athlete import Athlete
import repositories.athlete_repository as athlete_repository
import repositories.event_repository as event_repository

athlete_blueprint = Blueprint("athletes", __name__)

@athlete_blueprint.route("/athletes")
def athletes():
    athletes = athlete_repository.select_all()
    return render_template("athlete/index.html", athletes = athletes)

@athlete_blueprint.route("/athlete/<id>")
def show (id):
    athlete = athlete_repository.select(id)
    events = event_repository.event_participation(athlete)
    return render_template('athlete/show.html', athlete = athlete)