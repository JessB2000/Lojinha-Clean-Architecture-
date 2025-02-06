from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.user.entity.user import User as UserModel
from app.infra.enum.store_enum import UserRole
from app.infra.security.hashing import HashUser


class RegisterUserUseCase():
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_data: dict):
        db_user = self.db.query(UserModel).filter(
            UserModel.email == user_data['email']).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email já registrado")

        hashed_password = HashUser.bcrypt(user_data['password'])

        new_user = UserModel(
            username=user_data['username'],
            email=user_data['email'],
            hashed_password=hashed_password,
            role=UserRole.USER if user_data.get(
                'is_admin', False) is False else UserRole.ADMIN
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
