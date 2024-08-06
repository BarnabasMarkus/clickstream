#!/usr/bin/env python3

from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from pydantic import BaseModel
from typing import List, Optional, Dict
from models import ClickStream, engine, init_db

app = FastAPI()

# Initialize the database
init_db()

# Dependency to get DB session
def get_session():
    with Session(engine) as session:
        yield session

# Pydantic model for request body
class ClickStreamCreate(BaseModel):
    user_id: str
    page_url: str
    referrer_url: str
    user_agent: str
    event_type: str
    object_id: Optional[str] = None

# Endpoint to collect clickstream data
@app.post("/collect/")
async def collect_clickstream(click: ClickStreamCreate, session: Session = Depends(get_session)):
    db_click = ClickStream.from_orm(click)
    session.add(db_click)
    session.commit()
    session.refresh(db_click)
    return db_click

# Endpoint to retrieve all clickstream data
@app.get("/clicks/", response_model=List[ClickStreamCreate])
async def get_clickstreams(session: Session = Depends(get_session)):
    statement = select(ClickStream)
    results = session.exec(statement).all()
    return results

# Run the application with: uvicorn main:app --reload
