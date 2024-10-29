from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app import models, schemas

def create(db: Session, anime: schemas.AnimeCreate):
    db_anime = db.query(models.Anime).filter(anime.name == models.Anime.name).first()
    if db_anime:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Anime already registered')
        
    db_anime = models.Anime(**anime.model_dump())
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime

def get_all(db: Session):
    return db.query(models.Anime).all()

def get_by_id(db: Session, id: int):
    search = db.query(models.Anime).filter(models.Anime.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Anime not found')
    return search

def update_by_id(db: Session, id: int, anime: schemas.AnimeCreate):
    search = db.query(models.Anime).filter(models.Anime.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Anime not found')
    search.name = anime.name
    search.name_jp = anime.name_jp
    search.name_br = anime.name_br
    search.synopsis = anime.synopsis
    db.commit()
    db.refresh(search)
    return search

def delete_by_id(db: Session, id: int):
    search = db.query(models.Anime).filter(models.Anime.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Anime not found')
    db.delete(search)
    db.commit()
    return