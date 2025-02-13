from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.user.infra.database.models.user_model import UserModel
from app.infra.enum.store_enum import UserRole
from app.user.infra.security.hashing import HashUser


class RegisterUserUseCase():
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_data: dict):
        db_user = self.db.query(UserModel).filter(
            UserModel.email == user_data['email']).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email já registrado")

        hashed_password = HashUser.bcrypt(user_data['password'])

        user_role = UserRole[user_data['type_user']]  

        new_user = UserModel(
            username=user_data['username'],
            email=user_data['email'],
            password=hashed_password,
            type_user=user_role
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
