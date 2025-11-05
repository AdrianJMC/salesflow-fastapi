# app/models/sale.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.core.database import Base

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    client = Column(String(100), nullable=False)
    product = Column(String(100), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    total = Column(Float, nullable=False)
