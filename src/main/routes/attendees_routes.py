from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeeHandler

attendees_route_bp = Blueprint("attendees_route", __name__)

@attendees_route_bp.route("/events/<event_id>/register", methods=["POST"])
def create_attendees(event_id: str):
    http_request = HttpRequest(query_params={"event_id": event_id}, body=request.json)
    attendee_handler = AttendeeHandler()

    http_response = attendee_handler.register(http_request)
    return jsonify(http_response.body), http_response.status_code

@attendees_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendee_badge(attendee_id: str):
    attendee_handler = AttendeeHandler()
    http_request = HttpRequest(query_params={"attendee_id": attendee_id})
    http_response = attendee_handler.get_attendee_badge(http_request)

    return jsonify(http_response.body), http_response.status_code