from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    password: str

class UserOut(BaseModel):
    username: str
    email: str

class UserLogin(BaseModel):
    username: str
    password: str
    