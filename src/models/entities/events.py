from dataclasses import dataclass
from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer

@dataclass
class Events(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)

    def __repr__(self):
        return f"Events object with data: [title={self.title}, maximum_attendees={self.maximum_attendees}]"