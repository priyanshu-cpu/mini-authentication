from fastapi import APIRouter, Depends, HTTPException
from dependencies.auth import get_current_user
from database import get_db
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserOut, UserUpdate
from utils.security import get_password_hash


router = APIRouter(prefix="/users")


@router.get("/me",response_model=UserOut)
def get_me(user: User = Depends(get_current_user)):
    return user

@router.put("/me", response_model=UserOut)
def update_me(body: UserUpdate ,user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    if body.username is not None:
        existing_user = db.query(User).filter(User.username == body.username, User.id == user.id).first()
        if existing_user:
            raise HTTPException(status_code=409, detail="username aleady exists")
        user.username = body.username

    if body.email is not None:
        existing_email = db.query(user).filter(user.email == body.email, User.id == user.id).first()
        if existing_email:
            raise HTTPException(status_code=409, detail="email already exists")
        user.email = body.email

    if body.password is not None:
        user.password_hash = get_password_hash(body.password)

    db.commit()
    db.refresh(user)
    return user

@router.delete("/me")
def delete_me():
    pass
