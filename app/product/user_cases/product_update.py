from sqlalchemy.orm import Session
from app.infra.database.models.product_model import ProductModel
from app.schemas.product import ProductUpdate
from app.infra.enum.store_enum import UserRole
from fastapi import HTTPException


class ProductUpdateUseCase:
    def __init__(self, db: Session):
        self.db = db

    def update_product(self, product_id: int, product_data: ProductUpdate, 
                       current_user):
        if current_user.role != UserRole.ADMIN:
            raise HTTPException(
                status_code=403, detail="Apenas adm pode atualizar produtos")

        product = self.db.query(ProductModel).filter(
            ProductModel.id == product_id).first()

        if not product:
            raise HTTPException(
                status_code=404, detail="Produto não encontrado")

        for key, value in product_data.dict(exclude_unset=True).items():
            setattr(product, key, value)

        self.db.commit()
        self.db.refresh(product)
        return product
