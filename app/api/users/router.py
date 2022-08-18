from fastapi import APIRouter, Depends

from app.commons.dependices import get_db_session

from .schema import UserCreateRequest, UserLoginoResponse, UserLoginRequest
from .services.add_new_user import add_new_user_
from .services.login import login_

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.post("")
def add_new_user(
    body: UserCreateRequest,
    db_session=Depends(get_db_session),
):
    return add_new_user_(body, db_session)


@user_router.post("/login", response_model=UserLoginoResponse)
def login(
    body: UserLoginRequest,
    db_session=Depends(get_db_session),
):
    return login_(body, db_session)
