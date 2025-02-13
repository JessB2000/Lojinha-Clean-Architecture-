from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.infra.database.session import Base

class CartItemModel(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    id_cart = Column(Integer, ForeignKey("carts.id"), nullable=False)
    id_products = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    cart = relationship("CartModel", back_populates="items")  
    product = relationship("ProductModel", back_populates="cart_items") 