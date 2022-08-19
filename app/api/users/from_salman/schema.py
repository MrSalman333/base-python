from pydantic import BaseModel


class UserLoginoResponse(BaseModel):
    access_token: str


class UserCreateRequest(BaseModel):
    username: str
    password: str


class UserLoginRequest(BaseModel):
    username: str
    password: str
