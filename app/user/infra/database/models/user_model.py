from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from app.infra.enum.store_enum import UserRole

from app.infra.database.session import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    type_user = Column(Enum(UserRole), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    active = Column(Boolean, default=True)

    cart = relationship("CartModel", back_populates="owner", uselist=False)
