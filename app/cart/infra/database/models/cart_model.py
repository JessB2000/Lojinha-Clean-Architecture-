from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.infra.database.session import Base


class CartModel(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    active = Column(Boolean, default=True)

    owner = relationship("UserModel", back_populates="cart")

    items = relationship("CartItemModel", back_populates="cart", cascade="all, delete-orphan", lazy="dynamic")
