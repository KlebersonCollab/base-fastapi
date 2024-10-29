from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app import models, schemas

async def create(db: Session, season: schemas.SeasonCreate):
    db_season = db.query(models.Season).filter(season.name == models.Season.name).first()
    if db_season:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Season already registered')
        
    db_season = models.Season(**season.model_dump())
    db.add(db_season)
    db.commit()
    db.refresh(db_season)
    return db_season

async def get_all(db: Session):
    return db.query(models.Season).all()

async def get_by_id(db: Session, id: int):
    search = db.query(models.Season).filter(models.Season.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Season not found')
    return search

async def update_by_id(db: Session, id: int, season: schemas.SeasonCreate):
    search = db.query(models.Season).filter(models.Season.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Season not found')
    search.number = season.number
    search.name = season.name
    search.year = season.year
    db.commit()
    db.refresh(search)
    return search

async def delete_by_id(db: Session, id: int):
    search = db.query(models.Season).filter(models.Season.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Season not found')
    db.delete(search)
    db.commit()
    return