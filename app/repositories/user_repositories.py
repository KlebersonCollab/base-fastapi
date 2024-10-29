from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app import models, schemas
 
from app.security.hashing import Hashing

async def create(db: Session, User: schemas.UserSchema):
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

async def login(email: str, password: str, db: Session):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    if not Hashing.verify(password, db_user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid password')
    return {'message': 'Login successful'}

async def get_all(db: Session):
    return db.query(models.User).all()

async def get_by_email(email: str, db: Session):
    search = db.query(models.User).filter(models.User.email == email).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return search

async def get_by_id(id: int, db: Session):
    search = db.query(models.User).filter(models.User.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return search

async def update_by_email(email: str, User: schemas.UserSchema, db: Session):
    search = db.query(models.User).filter(models.User.email == email).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    search.username = User.username
    search.email = User.email
    search.full_name = User.full_name
    db.commit()
    db.refresh(search)
    return search

async def delete_by_email(email: str, db: Session):
    search = db.query(models.User).filter(models.User.email == email).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    db.delete(search)
    db.commit()
    return