from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.user.entity.user import User as UserModel
from app.infra.enum.store_enum import UserRole


class DeleteUserUseCase():
    def __init__(self, db: Session):
        self.db = db

    def user_delete(self, user_id: int):
        user_to_delete = self.db.query(UserModel).filter(
            UserModel.id == user_id).first()
        if not user_to_delete:
            raise HTTPException(
                status_code=404, detail="Usuário não encontrado")

        if user_to_delete.role != UserRole.ADMIN:
            raise HTTPException(
                status_code=403, 
                detail="Apenas administradores podem excluir usuários")

        self.db.delete(user_to_delete)
        self.db.commit()
        return {"message": "Usuário deletado com sucesso"}
