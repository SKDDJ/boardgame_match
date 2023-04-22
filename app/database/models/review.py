from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    comment = Column(String)
    reviewer_id = Column(Integer, ForeignKey("users.id"))
    reviewed_id = Column(Integer, ForeignKey("users.id"))

    reviewer = relationship("User", foreign_keys=[reviewer_id], back_populates="given_reviews")
    reviewed = relationship("User", foreign_keys=[reviewed_id], back_populates="received_reviews")

