from pydantic import BaseModel
from datetime import datetime
from typing import List  


class CouponCodeResponse(BaseModel):
    id: int
    name: str
    price: int


class CouponCodeList(BaseModel):
    couponcodes: List[CouponCodeResponse]



class CouponCodeRequest(BaseModel):
   
    name: str
    price:int


