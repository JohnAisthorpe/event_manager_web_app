from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.athlete import Athlete
import repositories.athlete_repository as athlete_repository
import repositories.event_repository as event_repository

athlete_blueprint = Blueprint("athletes", __name__)

@athlete_blueprint.route("/athletes")
def athletes():
    athletes = athlete_repository.select_all()
    return render_template("athletes/index.html", athletes = athletes)

@athlete_blueprint.route("/athletes/<id>")
def show(id):
    athlete = athlete_repository.select(id)
    events = event_repository.event_athlete(athlete)
    return render_template("athletes/show.html", event = events, athlete = athlete)

# new athlete form
@athlete_blueprint.route("/athletes/new", methods = ['GET'])
def new_athlete():
    athletes = athlete_repository.select_all()
    events = event_repository.select_all()
    return render_template("athletes/new.html", athletes = athletes, events = events)

# new athlete submit 
@athlete_blueprint.route("/athletes", methods=['POST'])
def create_athlete():
    
    # Extract the request data
    name = request.form.get('name')

    # Create a new athlete object
    athlete = Athlete(name=name)

    # Add the athlete to the database
    athlete_repository.save(athlete)

    # Return a response with the new athlete's information
    return redirect('/athletes')

# edit page
@athlete_blueprint.route("/athletes/<id>/edit", methods=['GET'])
def edit_athlete(id):
    athlete = athlete_repository.select(id)
    return render_template('athletes/edit.html', athlete = athlete)

# submit edit (update)
@athlete_blueprint.route("/athletes/<id>", methods=['POST'])

def update_athlete(id):
    name = request.form['name']
    athlete = Athlete(name, id)
    athlete_repository.update(athlete)
    return redirect('/athletes')

