from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.commons.settings import config

from ..helpers import hash_password
from ..models import User
from ..schema import UserLoginRequest


def login_(
    body: UserLoginRequest,
    db_session: Session,
):

    stmt = select(User).where(
        User.username == body.username,
        User.hashed_password == hash_password(body.password),
    )
    user: User | None = db_session.execute(stmt).scalar_one_or_none()

    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    access_token = genrate_jwt_for_user(user)

    return {"access_token": access_token}


def genrate_jwt_for_user(user: User):
    now = datetime.now()
    token_expire_at = now + timedelta(seconds=config.AUTH_TOKEN_EXPIRE_IN)
    payload = {
        "sub": user.id,
        "username": user.username,
        "iat": int(now.timestamp()),
        "exp": int(token_expire_at.timestamp()),
    }

    encoded_jwt = jwt.encode(payload, key=config.AUTH_JWT_KEY, algorithm="HS256")
    return encoded_jwt
