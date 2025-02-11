from sqlalchemy.orm import Session
from app.infra.database.models.cartitem_model import CartItemModel
from fastapi import HTTPException


class RemoveProductCartUseCase:
    def __init__(self, db: Session):
        self.db = db

    def delete_product_cart(self, user_id: int, product_id: int):
        cart_item = self.db.query(CartItemModel).join(CartItemModel.cart).filter(
            CartItemModel.product_id == product_id, CartItemModel.cart.has(
                user_id=user_id)
        ).first()

        if not cart_item:
            raise HTTPException(
                status_code=404, detail="Produto não encontrado no carrinho")

        self.db.delete(cart_item)
        self.db.commit()

        return {"message": "Produto removido do carrinho com sucesso"}
