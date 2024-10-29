from sqlalchemy import Column, Boolean, DateTime
from sqlalchemy.ext.declarative import as_declarative
import datetime

@as_declarative()
class BestPractices:
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    active = Column(Boolean, default=True)