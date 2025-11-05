# app/schemas/sale.py
from datetime import datetime
from pydantic import BaseModel, Field

class SaleBase(BaseModel):
    client: str = Field(..., min_length=2)
    product: str = Field(..., min_length=2)
    total: float = Field(..., gt=0)

class SaleCreate(SaleBase):
    date: datetime = Field(default_factory=datetime.utcnow)

class SaleResponse(SaleBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True   # si usas pydantic v2: from_attributes = True
