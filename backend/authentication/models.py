from sqlalchemy import Column, String, Integer
from utils.baseModels import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    profile_picture = Column(String)
    password = Column(String)

    def __str__(self):
        return f"{self.full_name}"
