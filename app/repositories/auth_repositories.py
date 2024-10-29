from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm
from app import models
 
from app.config.jwt import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from app.schemas.auth_schema import TokenData
from app.security.hashing import Hashing

def login(user:OAuth2PasswordRequestForm, db: Session):
    db_user = db.query(models.User).filter(models.User.email == user.username).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    if not Hashing.verify(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid password')
    
    access_token = create_access_token(
        data={'sub': db_user.email}
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def verify_token(token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception