from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database.database import get_db

router = APIRouter()

@router.post('/anime/', status_code=status.HTTP_201_CREATED, response_model=schemas.AnimeOut, tags=['Animes'])
async def create_anime(anime: schemas.AnimeCreate, db: Session = Depends(get_db)):
    db_anime = db.query(models.Anime).filter(anime.name == models.Anime.name).first()
    if db_anime:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Anime already registered')
        
    db_anime = models.Anime(**anime.model_dump())
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime

@router.get('/anime/', response_model=list[schemas.AnimeOut], tags=['Animes'])
async def get_all_animes(db: Session = Depends(get_db)):
    return db.query(models.Anime).all()

@router.get('/anime/{id}', response_model=schemas.AnimeOut, tags=['Animes'])
async def get_anime_by_id(id: int, db: Session = Depends(get_db)):
    search = db.query(models.Anime).filter(models.Anime.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Anime not found')
    return search

@router.put('/anime/{id}', response_model=schemas.AnimeOut, tags=['Animes'])
async def update_anime_by_id(id: int, Anime: schemas.AnimeCreate, db: Session = Depends(get_db)):
    search = db.query(models.Anime).filter(models.Anime.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Anime not found')
    search.name = Anime.name
    search.name_jp = Anime.name_jp
    search.name_br = Anime.name_br
    search.synopsis = Anime.synopsis
    db.commit()
    db.refresh(search)
    return search

@router.delete('/anime/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Animes'])
async def delete_anime_by_id(id: int, db: Session = Depends(get_db)):
    search = db.query(models.Anime).filter(models.Anime.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Anime not found')
    db.delete(search)
    db.commit()
    return