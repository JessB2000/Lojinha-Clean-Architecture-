from pydantic import BaseModel


class CartUpdateItem(BaseModel):
    quantity: int