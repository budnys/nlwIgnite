import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

def test_insert_event():
    event = {
        "uuid": "meu-uuid",
        "title": "meu title",
        "slug": "meu-alug",
        "maximum_attendees": 50
    }
    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)

def test_get_event_by_id():
    event_id = "meu-uuid"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)