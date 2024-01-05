from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.orm import relationship

from utils.baseModels import BaseModelMixin
from enum import Enum as PyEnum
from db import Base, Session


class UserType(PyEnum):
    admin = "admin"
    editor = "editor"
    manager = "manager"


class User(Base, BaseModelMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, nullable=True)
    phone_number = Column(String, unique=True, nullable=True)
    user_type = Column(Enum(UserType), nullable=True, default=UserType.editor)
    profile_picture = Column(String, nullable=True)
    password = Column(String)

    workspace = relationship("Workspace", back_populates="user")

    def __str__(self):
        return f"{self.full_name}"

    def save(self, db: Session):
        db.add(self)
        db.commit()
        db.refresh(self)
        