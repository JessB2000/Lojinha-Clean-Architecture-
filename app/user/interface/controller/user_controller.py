from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.user.infra.database.session import db_get
from app.user.interface.adapter.schemas.user_create import UserCreate
from app.user.interface.adapter.schemas.user_update import UserUpdate
from app.user.interface.adapter.schemas.user_login import UserLogin
from app.user.user_cases.user_register import RegisterUserUseCase
from app.user.user_cases.user_update import UpdateUserUseCase
from app.user.user_cases.user_delete import DeleteUserUseCase
from app.user.user_cases.user_login import LoginUserUseCase
from app.user.user_cases.user_lists import ListUsersUseCase
from app.infra.enum.store_enum import UserRole
from app.user.interface.adapter.schemas.user_lists import UserList
from app.user.infra.web.dependencies import get_current_user

router = APIRouter()


@router.get("/", response_model=list[UserList])
def list_users(
    db: Session = Depends(db_get),
    current_user=Depends(get_current_user)
):
    list_users_use_case = ListUsersUseCase(db)
    print(current_user.type_user)
    return list_users_use_case.list_users(request_user_role=current_user.type_user)


@router.post("/user")
def create_user(user: UserCreate, db: Session = Depends(db_get)):
    register_use_case = RegisterUserUseCase(db)
    print(user.type_user)
    new_user = register_use_case.register_user(user.dict())
    return new_user


@router.put("/update/{user_id}")
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(db_get)):
    update_use_case = UpdateUserUseCase(db)
    updated_user = update_use_case.update_user(user_id, user.dict())
    return updated_user


@router.delete("/delete/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(db_get),
    current_user=Depends(get_current_user)
):
    delete_use_case = DeleteUserUseCase(db)

    return delete_use_case.user_delete(
        user_id=user_id,
        request_user_id=current_user.id,
        request_user_role=current_user.type_user
    )


@router.post("/login")
def login_user(data: UserLogin, db: Session = Depends(db_get)):
    login_use_case = LoginUserUseCase(db)
    return login_use_case.login_user(data.email, data.password)
