from pydantic import BaseModel, EmailStr
from app.infra.enum.store_enum import UserRole


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    type_user: UserRole
    active: bool

    class Config:
        use_enum_values = True  