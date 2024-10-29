from passlib.context import CryptContext


class Hashing():
    
    def encrypt(password: str) -> str:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashedPassword = pwd_context.hash(password)
        return hashedPassword
    
    def verify(password: str, hashed_password: str) -> bool:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.verify(password, hashed_password)