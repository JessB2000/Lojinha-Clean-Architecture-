from pydantic import BaseModel, EmailStr
from app.infra.enum.store_enum import UserRole


class UserResponse(BaseModel):
    id: int
    type_user = UserRole
    username: str
    email: EmailStr

    class Config:
        from_attributes = True