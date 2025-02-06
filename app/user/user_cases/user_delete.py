from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.user.entity.user import User as UserModel
from app.infra.enum.store_enum import UserRole


class DeleteUserUseCase():
    def __init__(self, db: Session):
        self.db = db

    def user_delete(self, user_id: int, request_user_id: int,
                    request_user_role: str):
        user_to_delete = self.db.query(UserModel).filter(
            UserModel.id == user_id).first()
        if not user_to_delete:
            raise HTTPException(
                status_code=404, detail="Usuário não encontrado")

        if request_user_id != user_id and request_user_role != UserRole.ADMIN:
            raise HTTPException(
                status_code=403, detail="Permissão negada")

        self.db.delete(user_to_delete)
        self.db.commit()
        return {"message": "Usuário deletado com sucesso"}
