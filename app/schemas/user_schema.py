from typing import Optional
from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    class Config():
        from_attributes = True
    
class ShowUserSchema(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    
    class Config:
        from_attributes = True