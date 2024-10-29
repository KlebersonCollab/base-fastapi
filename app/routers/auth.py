from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database.database import get_db
from app.security.hashing import Hashing

router = APIRouter()

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserSchema)
async def create_user(User: schemas.UserSchema, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(User.email == models.User.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='E-Mail already registered')
        
    db_user = models.User(
        username=User.username, 
        email=User.email, 
        full_name=User.full_name,
        password=Hashing.encrypt(User.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get('/login/', status_code=status.HTTP_200_OK)
async def login_user(email: str, password: str, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    if not Hashing.verify(password, db_user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid password')
    return {'message': 'Login successful'}

@router.get('/user/', response_model=list[schemas.ShowUserSchema])
async def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get('/user/{email}', response_model=schemas.ShowUserSchema)
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    search = db.query(models.User).filter(models.User.email == email).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return db.query(models.User).filter(models.User.email == email).first()

@router.get('/user/{id}/', response_model=schemas.ShowUserSchema)
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    search = db.query(models.User).filter(models.User.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return search

@router.put('/user/{email}', response_model=schemas.ShowUserSchema)
async def update_user_by_email(email: str, User: schemas.UserSchema, db: Session = Depends(get_db)):
    search = db.query(models.User).filter(models.User.email == email).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    search.username = User.username
    search.email = User.email
    search.full_name = User.full_name
    db.commit()
    db.refresh(search)
    return search

@router.delete('/user/{email}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_by_email(email: str, db: Session = Depends(get_db)):
    search = db.query(models.User).filter(models.User.email == email).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    db.delete(search)
    db.commit()
    return

