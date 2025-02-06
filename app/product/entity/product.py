from pydantic import BaseModel, Field
from app.frameworks.enum.store_enum import ProductCategory


class Product(BaseModel):
    id: int
    name: str
    description: str = Field(..., min_length=3, max_length=200)
    price: float = Field(..., gt=0)
    qt_stock: int
    active: bool = True
    category: ProductCategory
