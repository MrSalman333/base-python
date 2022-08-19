from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..helpers import hash_password
from ..models import User
from ..schema import UserCreateRequest


def add_new_user_(
    body: UserCreateRequest,
    db_session: Session,
):

    db_session.add(
        User(
            hashed_password=hash_password(body.password),
            username=body.username,
        )
    )

    try:
        db_session.flush()
    except IntegrityError:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "username already used")
