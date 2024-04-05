import pytest
from src.models.settings.connection import db_connection_handler
from .attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()

def test_insert_attendee():
    attendee = {
        "uuid": "meu-uuid-attendee",
        "name": "Diego",
        "email": "diego@diego.com",
        "event_id": "meu-uuid"
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendee)
    print(response)

def test_get_attendee_by_id():
    attendee_id = "meu-uuid-attendee"
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendee_badge_by_id(attendee_id)
    print(response)