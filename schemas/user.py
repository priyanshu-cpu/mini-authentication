from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserCreateResponse(BaseModel):
    message: str
    user: UserOut