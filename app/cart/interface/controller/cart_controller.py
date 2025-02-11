from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infra.database.session import db_get
from app.infra.web.dependencies import get_current_user
from app.cart.user_cases.cart_add_products import AddProductCartUseCase
from app.cart.user_cases.cart_list_products import ViewCartUseCase
from app.cart.user_cases.card_delete_products import RemoveProductCartUseCase
from app.cart.user_cases.card_update_products import UpdateProductQuantityUseCase

router = APIRouter()


@router.post("/cart/add")
def add_product_to_cart(product_id: int, quantity: int,
                        db: Session = Depends(db_get),
                        current_user=Depends(get_current_user)):
    cart_product_create_use_case = AddProductCartUseCase(db)
    cart_product_create = cart_product_create_use_case.addProductCart(
        current_user.id, product_id, quantity)
    return cart_product_create


@router.get("/cart")
def view_cart(db: Session = Depends(db_get),
              current_user=Depends(get_current_user)):
    cart_view_products_use_case = ViewCartUseCase(db)
    cart_view_products = cart_view_products_use_case.viewCart(current_user.id)
    return cart_view_products


@router.delete("/cart/remove")
def remove_product_from_cart(product_id: int, db: Session = Depends(db_get),
                             current_user=Depends(get_current_user)):
    cart_remove_product_use_case = RemoveProductCartUseCase(db)
    cart_remove_product = cart_remove_product_use_case.deleteProductCart(
        current_user.id, product_id)
    return cart_remove_product


@router.put("/cart/update")
def update_product_quantity(product_id: int, quantity: int, 
                            db: Session = Depends(db_get), 
                            current_user=Depends(get_current_user)):
    cart_update_quantity_product_use_case = UpdateProductQuantityUseCase(db)
    cart_update_quantity_product = cart_update_quantity_product_use_case.updateProductQuantity(
        current_user.id, product_id, quantity)
    return cart_update_quantity_product
