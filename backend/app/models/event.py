from sqlalchemy import Column, Integer, String, JSON, DateTime, func
from pydantic import BaseModel, Field
from typing import Dict
from app.db import Base

# pyndantic model (api inp)
class EventIn(BaseModel):
    source: str = Field(..., example="auth-service")
    type: str = Field(..., example="user.login")
    payload: Dict = Field(..., example={"user_id": 123})

# sqlalchemy  (db schema)
class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    type = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())