
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from app import models, schemas 
from app.repositories import auth_repositories
from app.security.hashing import Hashing

def create(db: Session, User: schemas.UserSchema):
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

def get_all(db: Session):
    return db.query(models.User).all()

def get_by_email(email: str, db: Session):
    search = db.query(models.User).filter(models.User.email == email).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return search

def get_by_id(id: int, db: Session):
    search = db.query(models.User).filter(models.User.id == id).first()
    if not search:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return search