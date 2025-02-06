from sqlalchemy import Column, Integer, String, Boolean, Float, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.infra.enum.store_enum import ProductCategory

Base = declarative_base()


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
    qt_stock = Column(Integer, default=0)
    active = Column(Boolean, default=True)
    category = Column(Enum(ProductCategory), nullable=False)

    cart_items = relationship("CartItem", back_populates="product")