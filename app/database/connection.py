from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from app.config import DATABASE_URL


engine = create_engine(DATABASE_URL)

Base: MetaData = declarative_base()

def create_tables():
    Base.metadata.create_all(engine)
