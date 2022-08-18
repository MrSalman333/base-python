from typing import Optional

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.commons.settings import config

from .database import SessionLocal


def get_db_session():
    session: Session = SessionLocal()
    try:
        with session.begin():
            yield session
    except Exception:
        session.rollback()
    finally:
        session.close()


def get_verified_current_user_or_none(
    token: Optional[str] = Depends(OAuth2PasswordBearer(tokenUrl="user/login", auto_error=False))
):
    if token is None:
        return None

    try:
        varified_and_decoded_token = jwt.decode(token, config.AUTH_JWT_KEY, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return varified_and_decoded_token


def login_required(payload: Optional[dict] = Depends(get_verified_current_user_or_none)):
    """
    we are sure to have the token since we have auto_error = True
    """

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
