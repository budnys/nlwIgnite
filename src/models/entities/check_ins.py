from src.models.settings.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class CheckIns(Base):
    __tablename__ = "check_ins"

    id = Column(Integer, primary_key=True)
    attendee_id = Column(String, ForeignKey("attendees.id"))
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"CheckIns object with data: [attendee_id={self.attendee_id}]"