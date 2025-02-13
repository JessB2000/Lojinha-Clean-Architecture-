from pydantic import BaseModel, EmailStr
from app.infra.enum.store_enum import UserRole


class UserList(BaseModel):
    id: int
    username: str
    type_user: UserRole
    email: EmailStr
    active: bool

    class Config:
        orm_mode = True