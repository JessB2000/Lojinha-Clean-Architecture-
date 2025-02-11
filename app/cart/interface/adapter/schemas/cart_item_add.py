from pydantic import BaseModel


class CartAddItem(BaseModel):
    product_id: int
    quantity: int