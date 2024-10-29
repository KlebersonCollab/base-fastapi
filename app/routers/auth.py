from fastapi import Depends, APIRouter,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app import schemas
from app.database.database import get_db
from app.repositories import auth_repositories

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('/token/', status_code=status.HTTP_200_OK, response_model=schemas.Token)
def token(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth_repositories.login(user, db)

def get_current_user(token: str = Depends(oauth_scheme)):
    return auth_repositories.verify_token(token)