from typing import Optional
from fastapi import UploadFile, File, Form
from pydantic import BaseModel
from enum import Enum

class UserType(str, Enum):
    admin = 'admin'
    editor = 'editor'
    manager = 'manager'
    
class UserRegister(BaseModel):
    full_name : str = Form(...)
    password : str = Form(...)
    phone_number : str = Form(...)
    password : str = Form(...)
    profile_picture : Optional[UploadFile] = File(None)
    user_type : UserType = UserType

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    phone_number : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str
