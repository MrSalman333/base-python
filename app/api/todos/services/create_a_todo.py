from sqlalchemy.orm import Session

from ..models import Todo
from ..schema import TodoCreateRequest


def create_a_todo_(
    body: TodoCreateRequest,
    db_session: Session,
    current_user: dict,
):

    db_session.add(
        Todo(
            user_id=current_user["sub"],
            **body.dict(),
        )
    )
