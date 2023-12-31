from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import JSONResponse, Response
from fastapi.security import OAuth2PasswordRequestForm

from db import db_dependency
from authentication.schemas import UserRegister, Token
from authentication.models import User
from authentication.auth_utils import get_password_hash, authenticate_user
from authentication.jwt_utils import create_access_token, get_current_user
from utils.file_saving import save_file

router = APIRouter()


@router.post("/create-account")
async def user_register(db: db_dependency, user: UserRegister = Depends()):
    try:
        user_obj = db.query(User).filter(User.phone_number == user.phone_number).first()
        if user_obj is None:
            user_obj = User(
                full_name=user.full_name,
                phone_number=user.phone_number,
                password=get_password_hash(user.password),
                user_type=user.user_type,
            )
            if user.profile_picture is not None:
                user_obj.profile_picture = save_file(user.profile_picture)
            user_obj.save(db)
            return JSONResponse(
                {
                    "message": "User Created!",
                    "data": {
                        "id": user_obj.id,
                        "full_name": user_obj.full_name,
                        "phone_number": user_obj.phone_number,
                        "user_type": user_obj.user_type,
                        "profile_picture": user_obj.profile_picture,
                    },
                }
            )
        return JSONResponse({"message": "User already exsist!"})
    except Exception as e:
        return JSONResponse({"error": str(e)})


@router.post("/login", response_model=Token)
async def user_login(
    db: db_dependency, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        return JSONResponse({"message": "User Not Found!"})
    token = create_access_token(data={"user_id": user.id, "sub": user.phone_number})
    return JSONResponse({"access_token": token, "token_type": "bearer"})


@router.get("/get-user")
def get_user(db: db_dependency, user: Annotated[User, Depends(get_current_user)]):
    return {
        "user_id": user.id,
        "full_name": user.full_name,
        "phone_number": user.phone_number,
        "user_type": user.user_type,
        "profile_picture": user.profile_picture if user.profile_picture else None,
    }
