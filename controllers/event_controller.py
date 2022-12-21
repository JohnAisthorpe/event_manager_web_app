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
    athletes = athlete_repository.athlete_event(event)
    return render_template("events/show.html", event = event, athletes = athletes)

# new event form
@event_blueprint.route("/events/new", methods = ['GET'])
def new_event():
    events = event_repository.select_all()
    return render_template("events/new.html", events = events)

# new event submit 
@event_blueprint.route("/events", methods=['POST'])
def create_athlete():
    
    # Extract the request data
    name = request.form.get('name')
    sport = request.form.get('sport')

    # Create a new athlete object
    event = Event(name=name, sport=sport)

    # Add the athlete to the database
    event_repository.save(event)

    # Return a response with the new athlete's information
    return redirect('/events')

# edit page
@event_blueprint.route("/events/<id>/edit", methods=['GET'])
def edit_athlete(id):
    event = event_repository.select(id)
    return render_template('events/edit.html', event = event)

# submit edit (update)
@event_blueprint.route("/events/<id>", methods=['POST'])

def update_athlete(id):
    name = request.form['name']
    sport = request.form['sport']
    event = Event(name, sport, id)
    event_repository.update(event)
    return redirect('/events')