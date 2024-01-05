from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db import Base
from utils.baseModels import BaseModelMixin
from authentication.models import User

class Workspace(Base, BaseModelMixin):
    __tablename__ = "workspaces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="workspace")
    
    def __repr__(self):
        return f"<Workspace {self.name}>"
    
    def __str__(self):
        return self.name
    