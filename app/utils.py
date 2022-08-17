import configparser
import os
import sys
from datetime import datetime, timedelta
from typing import Any, Union

import bcrypt
from jose import jwt

from app.db.db import config


def get_hashed_password(password: str) -> str:
    hashed_bytes = bcrypt.kdf(
        password=password.encode("UTF-8"),
        salt=config.AUTH_SALT.encode("UTF-8"),
        desired_key_bytes=32,
        rounds=100,
    )

    password = str(hashed_bytes)
    return password


def verify_password(password: str, hashed_pass: str) -> bool:
    return get_hashed_password(password) == hashed_pass


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta:
        expires_delta = datetime.now() + expires_delta
    else:
        expires_delta = datetime.now() + timedelta(seconds=config.AUTH_TOKEN_EXPIRE_IN)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config.AUTH_JWT_KEY, config)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta:
        expires_delta = datetime.now() + expires_delta
    else:
        expires_delta = datetime.now() + timedelta(seconds=config.AUTH_REFRESH_TOKEN_EXPIRE_IN)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config.AUTH_JWT_KEY, config.ALGORITHM)
    return encoded_jwt
