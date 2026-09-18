from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from settings import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hash_password: str):
    return pwd_context.verify(plain_password, hash_password)


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "exp" : expire
    })

    token = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return token

def verify_token():
    pass