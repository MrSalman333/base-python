from sqlalchemy.orm import Session

from ..models import Todo
from ..schema import TodoCreateRequest


def create_a_todo_(
    body: TodoCreateRequest,
    db_session: Session,
):

    db_session.add(Todo(**body.dict()))
