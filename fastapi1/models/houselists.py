from pydantic import BaseModel
#from datetime import date
from decimal import Decimal
from typing import Optional
from enum import Enum


class HouseSold(str, Enum):
    SOLD_OUT = 'sold out'
    NOT_SOLD = 'not sold'

class HouseModel(BaseModel):
    house_number: int
    user_id: Optional[int]
    street: str
    price: Decimal
    description: Optional[str]
    sold: HouseSold
    


class HouseList(HouseModel):
    house_id: int
   
    
    class Config:
        orm_mode = True

class HouseCreate(HouseModel):
    pass
class HouseUpdate(HouseModel):
    pass