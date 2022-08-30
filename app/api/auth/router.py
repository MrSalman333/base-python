from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer

from .schema import (
    PublicUserResponse,
    UserCreateRequest,
    UserLoginRequest,
    UserLoginResponse,
    UserResponse,
    UserUpdateRequest,
)

auth_router = APIRouter(prefix="/user", tags=["user"])


@auth_router.post(
    path="",
    responses={
        status.HTTP_200_OK: {"description": "user created", "model": UserResponse},
        status.HTTP_409_CONFLICT: {"description": "username already used"},
    },
)
def signup_a_new_user(
    body: UserCreateRequest,
):
    """
    using this endpoint the user will regester a new account,
    """
    return {}


@auth_router.post(
    path="/login",
    responses={
        status.HTTP_200_OK: {"description": "valid credentials", "model": UserLoginResponse},
        status.HTTP_401_UNAUTHORIZED: {"description": "invalid credentials"},
    },
)
def login(
    body: UserLoginRequest,
):
    """
    using this endpoint the user will try to login with there username/password,
    """
    return {}


@auth_router.get(
    path="",
    response_model=list[PublicUserResponse],
)
def list_users():
    """
    list all of the users , returning public data only
    """
    return {}


@auth_router.get(
    path="/me",
    response_model=UserResponse,
    dependencies=[Depends(HTTPBearer())],
)
def get_current_user_data():
    """
    get the current user data
    """
    return {}


@auth_router.patch(
    path="/",
    response_model=UserResponse,
    dependencies=[Depends(HTTPBearer())],
)
def update_current_user_data(body: UserUpdateRequest):
    """
    update the current user data, if the key is not passed ,, it must be ignored
    """
    return {}
