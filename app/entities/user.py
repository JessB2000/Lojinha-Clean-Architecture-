from pydantic import BaseModel, EmailStr, Field

from app.frameworks.enum.store_enum import UserRole


class User(BaseModel):
    id: int
    type_user: UserRole
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str 
    active: bool = True
