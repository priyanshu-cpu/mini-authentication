from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from utils.security import create_token, verify_password, get_password_hash
from schemas.user import UserBase, UserLogin, UserCreateResponse
from database import get_db
from models.user import User


router = APIRouter(prefix="/auth")


@router.post("/register", response_model=UserCreateResponse)
def register_user(body: UserBase, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == body.username).first()
    if user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user already exists!")

    email = db.query(User).filter(User.email == body.email).first()
    if email is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already exists!")

    hash_password = get_password_hash(body.password)
    db_user = User(username = body.username,
                email = body.email,
                password_hash = hash_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        "message" : "user created successfully",
        "user" : db_user
    }

@router.post("/login")
def login_user(body: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == body.username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username!")
    if not verify_password(body.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password!")

    token = create_token({
        "sub" : str(user.id)
    })
    return {
        "access_token" : token,
        "token_type" : "bearer"
    }