from db.run_sql import run_sql
from models.event import Event
from models.athlete import Athlete

# save athlete to table
def save(athlete):
    sql = "INSERT INTO athlete(name) VALUES (%s) RETURNING id"
    values = [athlete.name]
    results = run_sql(sql, values)
    athlete.id = results[0]['id']
    return athlete

def select_all():
    athletes = []
    sql = "SELECT * FROM athlete"
    results = run_sql(sql)
    for row in results:
        athlete = Athlete(row['name'], row['id'])
        athletes.append(athlete)
    return athletes

def select(id):
    athlete = None
    sql = "SELECT * FROM athlete WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        athlete = Athlete(result['name'], result['id'])
    return athlete

def delete_all():
    sql = "DELETE FROM athlete"
    run_sql(sql)

def athlete_event(event):
    athletes = []
    sql = "SELECT athlete.* FROM athlete INNER JOIN participation ON Participation.athlete_id = athlete.id WHERE event_id = %s"
    values = [event.id]
    results = run_sql(sql, values)
    for row in results:
        athlete = Athlete(row['name'], row['id'])
        athletes.append(athlete)
    return athletes

def update(athlete):
    sql = "UPDATE athlete SET name = %s WHERE id = %s"
    values = [athlete.name, athlete.id]
    run_sql(sql, values)
