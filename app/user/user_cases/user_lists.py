from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.user.infra.database.models.user_model import UserModel
from app.infra.enum.store_enum import UserRole


class ListUsersUseCase():
    def __init__(self, db: Session):
        self.db = db

    def list_users(self, request_user_role: str):
        if request_user_role != UserRole.ADMIN:
            raise HTTPException(
                status_code=403, detail="Permissão negada"
            )

        users = self.db.query(UserModel).all()
        return users
