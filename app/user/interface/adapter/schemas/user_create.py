from pydantic import BaseModel, EmailStr
from app.infra.enum.store_enum import UserRole


class UserCreate(BaseModel):
    username: str
    type_user: UserRole
    email: EmailStr
    password: str
    active: bool = True