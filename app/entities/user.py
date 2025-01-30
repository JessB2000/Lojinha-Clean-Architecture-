from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str 
    active: bool = True
