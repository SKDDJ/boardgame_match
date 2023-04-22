from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    game_type = Column(String, index=True)
    location = Column(String)
    date_time = Column(DateTime)
    max_players = Column(Integer)
    host_id = Column(Integer, ForeignKey("users.id"))
    host = relationship("User", back_populates="hosted_events")
