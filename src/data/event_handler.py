import uuid
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repository.events_repository import EventsRepository

class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())

        event = self.__events_repository.insert_event(body)

        return HttpResponse(body=event, status_code=200)
    
    def get_by_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.q_params["event_id"]
        event = self.__events_repository.get_event_by_id(event_id)
        if not event:
            raise Exception("Evento nao encontrado")
        
        event_attendees_count = self.__events_repository.get_event_attendees(event_id)

        return HttpResponse(
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "details": event.details,
                    "slug": event.slug,
                    "maximum_attendees": event.maximum_attendees,
                    "current_total_attendees": event_attendees_count["attendees_amount"]
                }
            },
            status_code=200
        )