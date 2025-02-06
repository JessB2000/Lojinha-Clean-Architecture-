from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class ProductCategory(str, Enum):
    CLOTHING = "CLOTHING"
    ACCESSORIES = "ACCESSORIES"
