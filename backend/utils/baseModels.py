from datetime import datetime
from sqlalchemy import Column, DateTime
from db import Session

class BaseModelMixin:
	__abstract__ = True

	created_at = Column(DateTime, default=datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

	def save(self, db : Session):
		db.add(self)
		db.commit()
		db.refresh(self)
		return self	