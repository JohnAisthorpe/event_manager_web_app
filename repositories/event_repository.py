from db.run_sql import run_sql
from models.event import Event
from models.athlete import Athlete

# save event to table
def save(event):
    sql = "INSERT INTO event(name, sport) VALUES (%s, %s) RETURNING id"
    values = [event.name, event.sport]
    results = run_sql(sql, values)
    event.id = results[0]['id']
    return event

def select_all():
    events = []
    sql = "SELECT * FROM event"
    results = run_sql(sql)
    for row in results:
        event = Event(row['name'], row['sport'], row['id'])
        events.append(event)
    return events

def select(id):
    event = None
    sql = "SELECT * FROM event WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        location = Event(result['name'], result['sport'], result['id'])
    return event

def delete_all():
    sql = "DELETE FROM event"
    run_sql(sql)

