from pydantic import BaseModel
from typing import List
from app.cart.interface.adapter.schemas.cart_item_response import CartItemResponse


class CartResponseSchema(BaseModel):
    id: int
    user_id: int
    items: List[CartItemResponse]

    class Config:
        from_attributes = True