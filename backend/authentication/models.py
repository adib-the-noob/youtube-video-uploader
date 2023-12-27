from sqlalchemy import Column, String, Integer
from utils.baseModels import BaseModelMixin

from db import Base

class User(Base, BaseModelMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, nullable=True)
    phone_number = Column(String, unique=True, nullable=True)
    profile_picture = Column(String, nullable=True)
    password = Column(String)

    def __str__(self):
        return f"{self.full_name}"
