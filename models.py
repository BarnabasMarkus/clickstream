#!/usr/bin/env python3

from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Optional
import datetime

class ClickStream(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    page_url: str
    referrer_url: str
    user_agent: str
    event_type: str
    object_id: Optional[str] = None

DATABASE_URL = "sqlite:///./clickstream.db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
