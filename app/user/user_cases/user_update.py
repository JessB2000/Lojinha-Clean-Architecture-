from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.infra.database.models.user_model import UserModel
from app.infra.security.hashing import HashUser


class UpdateUserUseCase():
    def __init__(self, db: Session):
        self.db = db

    def update_user(self, user_id: int, user_data: dict):
        user_to_update = self.db.query(UserModel).filter(
            UserModel.id == user_id).first()
        if not user_to_update:
            raise HTTPException(status_code=404, detail="User not found")

        if user_data.get("email"):
            user_to_update.email = user_data["email"]

        if user_data.get("password"):
            user_to_update.hashed_password = HashUser.bcrypt(
                user_data["password"])

        self.db.commit()
        self.db.refresh(user_to_update)
        return user_to_update
