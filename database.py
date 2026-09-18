from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from utils.settings import settings

engine = create_engine(settings.DB_CONNECTION)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
