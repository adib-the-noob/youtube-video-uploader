from datetime import timedelta, datetime
from typing import Annotated

from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from config import config
from authentication.models import (
    User
)
from db import db_dependency 

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/login')

def create_access_token(data : dict, expires_delta : timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({
        'exp' : expire
    })
    encoded_jwt = jwt.encode(
        to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM
    )
    return encoded_jwt


def get_current_user(
    db : db_dependency,
    token : Annotated[str, Depends(oauth_scheme)]
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, config.SECRET_KEY, algorithms=[config.ALGORITHM]
        )
        phone_number = payload.get('sub')
        user = db.query(User).filter(
            User.phone_number == phone_number
        ).first()
        if user is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user