from pydantic import BaseModel
from typing import Optional
from infra.enum.store_enum import ProductCategory


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category: Optional[ProductCategory] = None