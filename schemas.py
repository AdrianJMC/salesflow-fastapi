from pydantic import BaseModel
from datetime import datetime

class SaleBase(BaseModel):
    client: str
    product: str
    total: float

class SaleCreate(SaleBase):
    date: datetime

class SaleResponse(SaleBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
