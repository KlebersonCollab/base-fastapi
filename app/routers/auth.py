from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app.database.database import get_db
from app.repositories import user_repositories

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserSchema)
async def create_user(User: schemas.UserSchema, db: Session = Depends(get_db)):
    return user_repositories.create(db, User)

@router.get('/login/', status_code=status.HTTP_200_OK)
async def login_user(email: str, password: str, db: Session = Depends(get_db)):
    return user_repositories.login(email, password, db)

@router.get('/user/', response_model=list[schemas.ShowUserSchema])
async def get_all_users(db: Session = Depends(get_db)):
    return user_repositories.get_all(db)

@router.get('/user/{email}', response_model=schemas.ShowUserSchema)
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return user_repositories.get_by_email(email, db)

@router.get('/user/{id}/', response_model=schemas.ShowUserSchema)
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return user_repositories.get_by_id(id, db)

@router.put('/user/{email}', response_model=schemas.ShowUserSchema)
async def update_user_by_email(email: str, User: schemas.UserSchema, db: Session = Depends(get_db)):
    return user_repositories.update_by_email(email, User, db)

@router.delete('/user/{email}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_by_email(email: str, db: Session = Depends(get_db)):
    return user_repositories.delete_by_email(email, db)

