import pdb
from models.participation import Participation
from models.athlete import Athlete
from models.event import Event
import repositories.event_repository as event_repository
import repositories.athlete_repository as athlete_repository
import repositories.participation_repository as participation_repository

# deleting contents of tables to prevent duplicates
participation_repository.delete_all()
event_repository.delete_all()
athlete_repository.delete_all()

# adding athlete to table
athlete1 = Athlete('Killian Jornet')
athlete_repository.save(athlete1)

athlete2 = Athlete('Courtney Douwalter')
athlete_repository.save(athlete2)

event1 = Event('UTMB', 'running')
event_repository.save(event1)

event2 = Event('Western States', 'running')
event_repository.save(event2)

# print(athlete_repository.select(11).__dict__)



participation1 = Participation(athlete1, event1)
participation_repository.save(participation1)
