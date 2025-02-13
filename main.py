from fastapi import FastAPI
from app.infra.database.session import Base, engine
from app.user.interface.controller.user_controller import router as user_router
from app.product.interface.controller.product_controller import router as product_router
from app.cart.interface.controller.cart_controller import router as cart_router
from app.cart.infra.database.models.cart_model import CartModel
from app.cart.infra.database.models.cartitem_model import CartItemModel
from app.product.infra.database.models.product_model import ProductModel
from app.user.infra.database.models.user_model import UserModel

Base.metadata.create_all(bind=engine)


app = FastAPI(title="E-commerce API")

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(cart_router, prefix="/cart", tags=["Cart"])


@app.get("/")
def health_check():
    return {"message": "API is running!"}
