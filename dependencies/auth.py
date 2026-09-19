from utils.security import credentials_exception
from models.user import User
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from utils.security import verify_token

def get_current_user(payload: dict = Depends(verify_token), db: Session = Depends(get_db)):
    try:
        user_id = int(payload["sub"])
    except (ValueError, TypeError, KeyError):
        raise credentials_exception
    user = db.get(User, user_id)

    if user is None:
        raise credentials_exception

    return user