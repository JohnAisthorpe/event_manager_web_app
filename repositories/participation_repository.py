from db.run_sql import run_sql
from models.participation import Participation
from models.event import Event
from models.athlete import Athlete
import repositories.athlete_repository as athlete_repository
import repositories.event_repository as event_repository

def save(participation):
    sql = "INSERT INTO participation (athlete_id, event_id)  VALUES (%s, %s, %s) RETURNING id"
    values = [participation.athlete.id, participation.event.id]
    results = run_sql(sql, values)
    participation.id = results[0]['id']
    return participation

def select_all():
    participations = []
    sql = "SELECT * FROM participation"
    results = run_sql(sql)
    for row in results:
        athlete = athlete_repository.select(row['athlete_id'])
        event = event_repository.select(row['event_id'])
        participation = Participation(athlete, event, row['id'])
        participations.append(participation)
    return participations

def delete_all():
    sql = "DELETE FROM participation"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM participation WHERE id = %s"
    values = [id]
    run_sql(sql, values)


