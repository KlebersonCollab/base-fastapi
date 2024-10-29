from typing import List, Optional
from pydantic import BaseModel

class AnimeCreate(BaseModel):
    name: str
    name_jp: str
    name_br: str
    synopsis: str
    image_url: str  # Campo para armazenar o caminho ou URL da imagem
    season_id: int
    by_id: int

class AnimeOut(BaseModel):
    id: int
    name: str
    name_jp: str
    name_br: str
    synopsis: str
    image_url: str  # Campo para armazenar o caminho ou URL da imagem
    season_id: int
    by_id: int

    class Config:
        from_attributes = True

class SeasonCreate(BaseModel):
    number: int
    name: str
    year: int

class SeasonOut(BaseModel):
    id: int
    number: int
    name: str
    year: int
    animes: List[AnimeOut] = []

    class Config:
        from_attributes = True