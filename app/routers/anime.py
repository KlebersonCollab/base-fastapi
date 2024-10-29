from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from app import schemas
from app.database.database import get_db
from app.repositories import anime_repositories

router = APIRouter(prefix='/animes/anime', tags=['Animes'])

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.AnimeOut, tags=['Animes'])
async def create_anime(anime: schemas.AnimeCreate, db: Session = Depends(get_db)):
    return anime_repositories.create(db, anime)

@router.get('/', response_model=list[schemas.AnimeOut], tags=['Animes'])
async def get_all_animes(db: Session = Depends(get_db)):
    return anime_repositories.get_all(db)

@router.get('/{id}', response_model=schemas.AnimeOut, tags=['Animes'])
async def get_anime_by_id(id: int, db: Session = Depends(get_db)):
    return anime_repositories.get_by_id(db, id)

@router.put('/{id}', response_model=schemas.AnimeOut, tags=['Animes'])
async def update_anime_by_id(id: int, Anime: schemas.AnimeCreate, db: Session = Depends(get_db)):
    return anime_repositories.update_by_id(db, id, Anime)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Animes'])
async def delete_anime_by_id(id: int, db: Session = Depends(get_db)):
    return anime_repositories.delete_by_id(db, id)