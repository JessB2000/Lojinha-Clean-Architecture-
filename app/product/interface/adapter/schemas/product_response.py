from pydantic import BaseModel
from typing import Optional
from app.infra.enum.store_enum import ProductCategory


class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    stock: int
    category: ProductCategory

    class Config:
        from_attributes = True