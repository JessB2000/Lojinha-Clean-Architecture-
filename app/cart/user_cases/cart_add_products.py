# app/use_cases/cart/add_product_to_cart.py
from sqlalchemy.orm import Session
from app.infra.database.models.cart_model import CartModel
from app.infra.database.models.cartitem_model import CartItemModel
from app.infra.database.models.product_model import ProductModel
from fastapi import HTTPException


class AddProductCartUseCase:
    def __init__(self, db: Session):
        self.db = db

    def add_product_cart(self, user_id: int, product_id: int, quantity: int):
        product = self.db.query(ProductModel).filter(
            ProductModel.id == product_id).first()
        if not product:
            raise HTTPException(
                status_code=404, detail="Produto não encontrado")

        cart = self.db.query(CartModel).filter(
            CartModel.user_id == user_id).first()
        if not cart:
            cart = CartModel(user_id=user_id)
            self.db.add(cart)
            self.db.commit()
            self.db.refresh(cart)

        cart_item = self.db.query(CartItemModel).filter(
            CartItemModel.cart_id == cart.id,
            CartItemModel.product_id == product_id
        ).first()

        if cart_item:
            raise HTTPException(
                status_code=400, detail="Produto já está no carrinho")

        new_cart_item = CartItemModel(
            cart_id=cart.id, product_id=product_id, quantity=quantity)
        self.db.add(new_cart_item)
        self.db.commit()
        self.db.refresh(new_cart_item)

        return new_cart_item
