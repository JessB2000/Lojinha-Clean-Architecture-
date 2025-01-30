from typing import List
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: int
    id_user: int
    items: List[int] = []
    quantity: List[int] = []