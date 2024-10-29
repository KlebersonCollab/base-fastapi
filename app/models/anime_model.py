# Description: Anime model class.
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base
from app.models.best_practices import BestPractices


class Anime(Base,BestPractices):
    __tablename__ = "animes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    name_jp = Column(String, unique=True, index=True)
    name_br = Column(String, unique=True, index=True)
    synopsis = Column(String)
    image_url = Column(String)  # Campo para armazenar o caminho ou URL da imagem
    season_id = Column(Integer, ForeignKey('seasons.id'))
    season = relationship("Season", back_populates="animes")
    by_id = Column(Integer, ForeignKey('users.id'))
    by = relationship('User', back_populates='animes')

class Season(Base,BestPractices):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    number = Column(Integer, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    year = Column(Integer)
    animes = relationship("Anime", back_populates="season")


    
