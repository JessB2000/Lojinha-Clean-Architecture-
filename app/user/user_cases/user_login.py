from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.user.infra.database.models.user_model import UserModel
from app.user.infra.security.hashing import HashUser
from app.user.infra.security.token_manager import create_access_token


class LoginUserUseCase():
    def __init__(self, db: Session):
        self.db = db

    def login_user(self, email: str, password: str):
        user = self.db.query(UserModel).filter(
            UserModel.email == email).first()
        if not user:
            raise HTTPException(
                status_code=401, detail="Credenciais inválidas")

        if not HashUser.verify(user.password, password):
            raise HTTPException(
                status_code=401, detail="Credenciais inválidas")

        token = create_access_token(data={"sub": user.email})
        return {"access_token": token, "token_type": "bearer"}
