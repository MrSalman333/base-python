import bcrypt

from app.commons.settings import config


def hash_password(password: str):
    hashed_bytes = bcrypt.kdf(
        password=password.encode("UTF-8"),
        salt=config.AUTH_SALT.encode("UTF-8"),
        desired_key_bytes=32,
        rounds=100,
    )

    password = str(hashed_bytes)
    return password
