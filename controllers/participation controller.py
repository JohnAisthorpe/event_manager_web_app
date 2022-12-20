from flask import Flask, render_template,request, redirect
from flask import Blueprint
from models.participation import Participation
import repositories.participation_repository as participation_repository 
import repositories.athlete_repository as athlete_repository 
import repositories.event_repository as event_repository

participation_blueprint = Blueprint("/participation", __name__)

@participation_blueprint.route("/participation")
def participation():
    participation = participation_repository.select_all()
    return render_template("participation/index.html", participation = participation)

@participation_blueprint.route("/participation", methods = ['GET'])
def new_participation():
    athletes = athlete_repository.select_all()
    events = event_repository.select_all()
    return render_template("participation/new.html", athletes = athletes, events = events)

@participation_blueprint
