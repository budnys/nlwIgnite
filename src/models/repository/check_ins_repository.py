from sqlalchemy.exc import IntegrityError
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns

class CheckInsRepository:
    def insert_check_in(self, attendeeId: str):
        with db_connection_handler as db:
            try:
                check_in = CheckIns(
                    attendee_id=attendeeId
                )
                db.session.add(check_in)
                db.session.commit()
            except IntegrityError:
                raise Exception('Checkin ja realizado!')
            except Exception as exception:
                db.session.rollback()
                raise exception