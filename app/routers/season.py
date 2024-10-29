from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database.database import get_db

router = APIRouter(prefix='/seasons/season', tags=['Season'])

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.SeasonOut)
async def create_season(season: schemas.SeasonCreate, db: Session = Depends(get_db)):
    db_season = db.query(models.Season).filter(season.name == models.Season.name).first()
    if db_season:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Season already registered')
        
    db_season = models.Season(**season.model_dump())
    db.add(db_season)
    db.commit()
    db.refresh(db_season)
    return db_season

@router.get('/', response_model=list[schemas.SeasonOut])
async def get_all_seasons(db: Session = Depends(get_db)):
    return db.query(models.Season).all()

@router.get('/{id}', response_model=schemas.SeasonOut)
async def get_season_by_id(id: int, db: Session = Depends(get_db)):
    search = db.query(models.Season).filter(models.Season.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Season not found')
    return search

@router.put('/{id}', response_model=schemas.SeasonOut)
async def update_season_by_id(id: int, Season: schemas.SeasonCreate, db: Session = Depends(get_db)):
    search = db.query(models.Season).filter(models.Season.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Season not found')
    search.number = Season.number
    search.name = Season.name
    search.year = Season.year
    db.commit()
    db.refresh(search)
    return search

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_season_by_id(id: int, db: Session = Depends(get_db)):
    search = db.query(models.Season).filter(models.Season.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Season not found')
    db.delete(search)
    db.commit()
    return