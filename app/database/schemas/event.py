
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventBase(BaseModel):
    title: str
    game_type: str
    location: str
    date_time: datetime
    max_players: int

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    host_id: int

    class Config:
        orm_mode = True

