from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.infra.database.session import db_get
from app.product.user_cases.product_create import ProductCreateUseCase
from app.product.user_cases.product_update import ProductUpdateUseCase
from app.product.user_cases.product_delete import ProductDeleteUseCase
from app.infra.web.dependencies import get_current_user
from app.schemas.product import ProductCreate, ProductUpdate

router = APIRouter()


@router.post("/products")
def create_product(product_data: ProductCreate, 
                   db: Session = Depends(db_get), current_user=Depends(get_current_user)):
    product_create_use_case = ProductCreateUseCase(db)
    product_create = product_create_use_case.create_product(
        product_data, current_user)
    return product_create


@router.put("/products/{product_id}")
def update_product(product_id: int, product_data: ProductUpdate, 
                   db: Session = Depends(db_get), current_user=Depends(get_current_user)):
    product_update_use_case = ProductUpdateUseCase(db)
    product_update = product_update_use_case.update_product(
        product_id, product_data, current_user)
    return product_update


@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(db_get), 
                   current_user=Depends(get_current_user)):
    product_delete_use_case = ProductDeleteUseCase(db)
    product_delete = product_delete_use_case.delete_product(
        product_id, current_user)
    return product_delete
