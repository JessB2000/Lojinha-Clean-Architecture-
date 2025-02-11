# app/use_cases/cart/view_cart.py
from sqlalchemy.orm import Session
from app.infra.database.models.cart_model import CartModel
from fastapi import HTTPException


class ViewCartUseCase:
    def __init__(self, db: Session):
        self.db = db

    def viewCart(self, user_id: int):
        cart = self.db.query(CartModel).filter(
            CartModel.user_id == user_id).first()
        if not cart or not cart.items:
            raise HTTPException(
                status_code=404, detail="O carrinho está vazio!")

        return cart.items
