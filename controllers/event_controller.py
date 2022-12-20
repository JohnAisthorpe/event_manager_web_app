from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.event import Event
import repositories.athlete_repository as athlete_repository
import repositories.event_repository as event_repository


event_blueprint = Blueprint("events", __name__)

@event_blueprint.route("/events")
def events():
    events = event_repository.select_all()
    return render_template("events/index.html", events = events)

@event_blueprint.route("/events/<id>")
def show(id):
    event = event_repository.select(id)
    athlete = athlete_repository.event_participation(event)
    return render_template("events/show.html", event = event, athlete = athlete)