from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    name: str
    email: str
    preferences: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    hosted_events: List[int]
    joined_events: List[int]

    class Config:
        orm_mode = True

