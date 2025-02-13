from sqlalchemy.orm import Session
from app.cart.infra.database.models.cartitem_model import CartItemModel
from fastapi import HTTPException


class UpdateProductQuantityUseCase:
    def __init__(self, db: Session):
        self.db = db

    def update_product_quantity(self, user_id: int, product_id: int, quantity: int):
        cart_item = self.db.query(CartItemModel).join(CartItemModel.cart).filter(
            CartItemModel.product_id == product_id, CartItemModel.cart.has(
                user_id=user_id)
        ).first()

        if not cart_item:
            raise HTTPException(
                status_code=404, detail="Produto não encontrado no carrinho")

        if quantity <= 0:
            raise HTTPException(
                status_code=400, detail="Quantidade de produtos insuficiente")

        cart_item.quantity = quantity
        self.db.commit()
        self.db.refresh(cart_item)

        return cart_item
