from pydantic import BaseModel
from datetime import datetime
from typing import List  


class AdminUserResponse(BaseModel):
    id: int
    name: str
    email: str
    createdat: datetime


class AdminUserRequest(BaseModel):
    name: str
    email: str

