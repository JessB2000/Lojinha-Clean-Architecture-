from sqlalchemy.orm import Session
from app.product.infra.database.models.product_model import ProductModel
from app.infra.enum.store_enum import UserRole
from fastapi import HTTPException


class ProductDeleteUseCase:
    def __init__(self, db: Session):
        self.db = db

    def delete_product(self, product_id: int, current_user):
        if current_user.role != UserRole.admin:
            raise HTTPException(
                status_code=403, detail="Apenas admin pode deletar produtos")

        product = self.db.query(ProductModel).filter(
            ProductModel.id == product_id).first()

        if not product:
            raise HTTPException(
                status_code=404, detail="Produto não encontrado")

        self.db.delete(product)
        self.db.commit()
        return {"message": "Produto deletado com sucesso"}
