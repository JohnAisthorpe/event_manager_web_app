from flask import Flask, render_template,request, redirect
from flask import Blueprint
from models.participation import Participation
import repositories.participation_repository as participation_repository 
import repositories.athlete_repository as athlete_repository 
import repositories.event_repository as event_repository

participation_blueprint = Blueprint("/participation", __name__)

@participation_blueprint.route("/participation")
def participation():
    participations = participation_repository.select_all()
    return render_template("participation/index.html", participations = participations)


# NEW participation
# GET '/participation/new'
@participation_blueprint.route("/participation/new", methods=['GET'])
def new_participation():
    athletes = athlete_repository.select_all()
    events = event_repository.select_all()
    return render_template("participation/new.html", athletes = athletes, events = events)

# CREATE
# POST '/participation'
@participation_blueprint.route("/participation",  methods=['POST'])
def create_participation():
    athlete_id = request.form['athlete_id']
    event_id = request.form['event_id']
    athlete = athlete_repository.select(athlete_id)
    event = event_repository.select(event_id)
    participation = Participation(athlete, event)
    participation_repository.save(participation)
    return redirect('/participation')

# # new participation form
# @participation_blueprint.route("/participation/new", methods = ['GET'])
# def new_participation():
#     participation = participation_repository.select_all()
#     return render_template("participation/new.html", participation =participation)

# # new event submit 
# @participation_blueprint.route("/participation", methods=['POST'])
# def create_participation():
    
#     # Extract the request data
#     athlete = request.form.get('athlete')
#     event = request.form.get('event')

#     # Create a new participation object

#     # Add the participation to the database
#     participation_repository.save(participation)

#     # Return a response with the new participation information
#     return redirect('/participation')
