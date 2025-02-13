from pydantic import BaseModel, Field
from typing import Optional
from app.infra.enum.store_enum import ProductCategory


class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price:  float = Field(..., gt=0)
    stock: int
    category: ProductCategory