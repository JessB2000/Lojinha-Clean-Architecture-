from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.product.entity.product import Product
from app.infra.enum.store_enum import UserRole


class ProductCreateUseCase:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product_data: ProductCreate, current_user):
        if current_user.role != UserRole.admin:
            raise HTTPException(status_code=403, detail="Apenas adm pode criar produtos")

        new_product = Product(**product_data.dict())

        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product