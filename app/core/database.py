# app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

USER = os.getenv("DB_USER", "root")
PASSWORD = os.getenv("DB_PASSWORD", "root")
HOST = os.getenv("DB_HOST", "localhost")
DB = os.getenv("DB_NAME", "salesflow")
PORT = os.getenv("DB_PORT", "3306")

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
