from pydantic import BaseModel
from app.product.interface.adapter.schemas.product_response import ProductResponse


class CartItemResponse(BaseModel):
    product: ProductResponse
    quantity: int

    class Config:
        from_attributes = True