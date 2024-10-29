from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from app import schemas
from app.database.database import get_db
from app.repositories import season_repositories

router = APIRouter(
    prefix='/seasons/season', 
    tags=['Season'],
    #Protege todas as Rotas
    dependencies=[Depends(season_repositories.get_current_user)]
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.SeasonOut)
async def create_season(season: schemas.SeasonCreate, db: Session = Depends(get_db)):
    return season_repositories.create(db, season)

@router.get('/', response_model=list[schemas.SeasonOut])
#Protege a Rota
async def get_all_seasons(db: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(season_repositories.get_current_user)):
    return season_repositories.get_all(db)

@router.get('/{id}', response_model=schemas.SeasonOut)
async def get_season_by_id(id: int, db: Session = Depends(get_db)):
    return season_repositories.get_by_id(db, id)

@router.put('/{id}', response_model=schemas.SeasonOut)
async def update_season_by_id(id: int, Season: schemas.SeasonCreate, db: Session = Depends(get_db)):
    return season_repositories.update_by_id(db, id, Season)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_season_by_id(id: int, db: Session = Depends(get_db)):
    return season_repositories.delete_by_id(db, id)