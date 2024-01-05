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
    profile_picture : UploadFile = File(None)
    user_type : UserType 


class UserLogin(BaseModel):
    phone_number : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str
