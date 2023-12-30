from fastapi import UploadFile, File, Form
from pydantic import BaseModel

class UserRegister(BaseModel):
    full_name : str = Form(...)
    password : str = Form(...)
    phone_number : str = Form(...)
    password : str = Form(...)
    profile_picture : UploadFile = File(None)


class UserLogin(BaseModel):
    phone_number : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str
