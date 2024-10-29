from fastapi import Depends, APIRouter,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from app import schemas
from app.database.database import get_db
from app.repositories import user_repositories
from app.routers.auth import get_current_user

router = APIRouter(prefix='/users', tags=['User'])

oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

@router.post('/user/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserSchema)
async def create_user(User: schemas.UserSchema, db: Session = Depends(get_db)):
    return user_repositories.create(db, User)

@router.get('/user/', response_model=list[schemas.ShowUserSchema])
async def get_all_users(db: Session = Depends(get_db)):
    return user_repositories.get_all(db)

@router.get('/user/{email}', response_model=schemas.ShowUserSchema)
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return user_repositories.get_by_email(email, db)

@router.get('/user/{id}/', response_model=schemas.ShowUserSchema)
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return user_repositories.get_by_id(id, db)
