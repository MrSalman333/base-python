from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.commons.settings import config

from .users.schemas import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/users/login")

async def get_verified_current_user(token: Optional[str] = Depends(oauth2_scheme)):
    if token is None:
        return None
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, config.AUTH_JWT_KEY, algorithms=[config.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        verified_and_decoded_token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    return verified_and_decoded_token_data


def login_required(payload: Optional[dict] = Depends(get_verified_current_user)):
    """
    we are sure to have the token since we have auto_error = True
    """

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
