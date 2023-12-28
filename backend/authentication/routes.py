from fastapi import APIRouter
from fastapi.responses import JSONResponse

from authentication.schemas import (
    UserRegister
)
from db import db_dependency
from authentication.models import (
    User
)
from authentication.auth_utils import (
    get_password_hash
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
                    "created_at" : str(user_obj.created_at)
                }
            })
        return JSONResponse({
            "message" : "User already exsist!"
        })
    except Exception as e:
        return JSONResponse({
            'error' : str(e)
        })