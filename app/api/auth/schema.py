from uuid import UUID

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str | None
    first_name: str
    last_name: str | None
    nationally: str | None
    bio: str | None


class PublicUserResponse(BaseModel):
    username: str
    first_name: str


class UserCreateRequest(BaseModel):
    first_name: str
    username: str
    password: str


class UserUpdateRequest(BaseModel):
    first_name: str | None
    last_name: str | None
    nationally: str | None
    bio: str | None
    email: str | None


class UserLoginResponse(BaseModel):
    access_token: str


class UserLoginRequest(BaseModel):
    username: str
    password: str
