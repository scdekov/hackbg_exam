from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


Base = declarative_base()
engine = create_engine("sqlite:///players.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)
