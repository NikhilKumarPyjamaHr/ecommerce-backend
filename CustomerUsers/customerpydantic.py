from pydantic import BaseModel
from datetime import datetime
from typing import List  


class CustomerUserResponse(BaseModel):
    id: int
    name: str
    email: str
    createdat: datetime


class CustomerUserList(BaseModel):
    customers: List[CustomerUserResponse]

class CustomerUserRequest(BaseModel):
    name: str
    email: str

