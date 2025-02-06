from typing import List
from pydantic import BaseModel


class Cart(BaseModel):
    id: int
    id_user: int
    items: List[int] = []
    quantity: List[int] = []