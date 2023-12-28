from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, Response
from fastapi.security import OAuth2PasswordRequestForm

from authentication.schemas import (
    UserRegister,
    UserLogin
)
from db import db_dependency
from authentication.models import (
    User
)
from authentication.auth_utils import (
    get_password_hash,
    authenticate_user
)

router = APIRouter()

@router.get('/t')
async def test():
    return JSONResponse({
        "message" : "welcome Bro!"
    })

@router.post('/create-account')
async def user_register(user : UserRegister, db : db_dependency):
    try:
        user_obj = db.query(User).filter(
            User.phone_number == user.phone_number
        ).first()
        if user_obj is None:
            user_obj = User(
                full_name=user.full_name,
                phone_number=user.phone_number,
                password=get_password_hash(user.password)
            )
            user_obj.save(db)
            return JSONResponse({
                "message" : "User Created!",
                "data" : {
                    "id" : user_obj.id,
                    "full_name" : user_obj.full_name,
                    "phone_number" : user_obj.phone_number
                }
            })
        return JSONResponse({
            "message" : "User already exsist!"
        })
    except Exception as e:
        return JSONResponse({
            'error' : str(e)
        })


@router.post('/login')
async def user_login(db : db_dependency, form_data : Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        return JSONResponse({
            "message" : "BRo!"
        })
    return JSONResponse({
        "message" : "Bro, just logged in!"
    })