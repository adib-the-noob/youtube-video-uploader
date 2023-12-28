from pydantic import BaseModel

class UserRegister(BaseModel):
    full_name : str
    password : str
    phone_number : str
    password : str


class UserLogin(BaseModel):
    phone_number : str
    password : str