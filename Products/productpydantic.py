from pydantic import BaseModel
from datetime import datetime
from typing import List  


class ProductResponse(BaseModel):
    id: int
    name: str
    description:str
    price:int
    admin_user_id: str


class ProductsList(BaseModel):
    products: List[ProductResponse]

class ProductRequest(BaseModel):
   
    name: str
    description:str
    price:int
    admin_user_id: str
