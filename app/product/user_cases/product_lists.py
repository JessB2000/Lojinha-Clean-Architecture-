from sqlalchemy.orm import Session
from app.product.infra.database.models.product_model import ProductModel


class ProductsListUseCase:
    def __init__(self, db: Session):
        self.db = db

    def list_products(self, page: int, category: str):
        query = self.db.query(ProductModel)
        if category:
            query = query.filter(ProductModel.category == category)

        products = query.limit(10).offset((page - 1) * 10).all()
        return products