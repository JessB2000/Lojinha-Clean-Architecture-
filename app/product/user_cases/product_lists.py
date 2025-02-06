from sqlalchemy.orm import Session
from app.product.entity.product import Product as ProductModel 


class ProductsListUseCase:
    def __init__(self, db: Session):
        self.db = db

    def execute(self, page: int, category: str):
        query = self.db.query(ProductModel)
        if category:
            query = query.filter(ProductModel.category == category)

        products = query.limit(10).offset((page - 1) * 10).all()
        return products