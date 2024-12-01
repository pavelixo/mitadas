# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.settings import DATABASE
from db.models import Base

engine = create_engine(DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(SessionLocal)

def get_session():
    return session

Base.metadata.create_all(engine)
