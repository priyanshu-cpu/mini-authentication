from utils.security import credentials_exception
from models.user import User

def get_current_user(payload: dict, db):
    try:
        user_id = int(payload["sub"])
    except (ValueError, TypeError, KeyError):
        raise credentials_exception
    user = db.get(User, user_id)

    if user is None:
        raise credentials_exception

    return user