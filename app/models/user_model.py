from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base
from app.models.best_practices import BestPractices


class User(Base, BestPractices):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    password = Column(String)
    animes = relationship("Anime", back_populates="by")
    

    
    
