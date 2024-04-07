from flask import Blueprint, jsonify, request
from src.errors.error_handler import handle_error
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeeHandler
from src.data.check_in_handler import CheckInHandler

check_in_route_bp = Blueprint("check_in_route", __name__)

@check_in_route_bp.route("/attendees/<attendee_id>/check-in", methods=["POST"])
def check_in_attendee(attendee_id: str):
    try:
        http_request = HttpRequest(query_params={"attendee_id": attendee_id})
        check_in_handler = CheckInHandler()

        http_response = check_in_handler.register(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
            http_response = handle_error(exception)
            return jsonify(http_response.body), http_response.status_code
