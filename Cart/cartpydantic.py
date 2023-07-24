from pydantic import BaseModel
from datetime import datetime
from typing import List  
  

class CartResponse(BaseModel):
    id: int
    items: str
    totalprice:int
    createdat:datetime
    purchasestatus: bool
    is_active: bool
    customer_user_id:str


class CartRequest(BaseModel):
   
    items: str
    totalprice:int
    purchasestatus: bool
    is_active: bool
    customer_user_id:str

class CartDeleteRequest(BaseModel):
   
    customer_user_id:str
