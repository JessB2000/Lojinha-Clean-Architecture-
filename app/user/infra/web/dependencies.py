import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.infra.database.session import db_get
from app.user.infra.database.models.user_model import UserModel
from dotenv import load_dotenv

load_dotenv("vars.env")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(db_get)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não é possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'),
                             algorithms=[os.getenv('ALGORITHM')])
        user_id: str = payload.get("sub")

        if user_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = db.query(UserModel).filter(UserModel.email == user_id).first()

    if user is None:
        raise credentials_exception

    return user
