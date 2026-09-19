from jose import jwt, JWTError
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from utils.settings import settings
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

bearer_schema = HTTPBearer(bearerFormat="JWT")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid or expired token!",
    headers={"WWW-Authenticate": "Bearer"}
)

password_hash = PasswordHash.recommended()

def get_password_hash(password: str):
    return password_hash.hash(password)

def verify_password(plain_password: str, hash_password: str):
    return password_hash.verify(plain_password, hash_password)


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "exp" : expire
    })

    token = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return token

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_schema)):
    try:
        payload = jwt.decode(credentials.credentials, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if not payload.get("sub"):
            raise credentials_exception
        return payload
    except JWTError:
        raise credentials_exception
