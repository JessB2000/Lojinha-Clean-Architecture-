from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infra.database.session import db_get
from app.user.interface.adapter.schemas.user_create import UserCreate
from app.user.interface.adapter.schemas.user_update import UserUpdate
from app.user.user_cases.user_register import RegisterUserUseCase
from app.user.user_cases.user_update import UpdateUserUseCase
from app.user.user_cases.user_delete import DeleteUserUseCase
from app.user.user_cases.user_login import LoginUserUseCase
from app.infra.web.dependencies import get_current_user

router = APIRouter()


@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(db_get)):
    register_use_case = RegisterUserUseCase(db)
    new_user = register_use_case.register_user(user.dict())
    return new_user


@router.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(db_get)):
    update_use_case = UpdateUserUseCase(db)
    updated_user = update_use_case.update_user(user_id, user.dict())
    return updated_user


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(db_get),
    current_user=Depends(get_current_user)
):
    delete_use_case = DeleteUserUseCase(db)

    return delete_use_case.user_delete(
        user_id=user_id,
        request_user_id=current_user.id,
        request_user_role=current_user.role
    )


@router.post("/login")
def login_user(email: str, password: str, db: Session = Depends(db_get)):
    login_use_case = LoginUserUseCase(db)
    return login_use_case.login_user(email, password)
