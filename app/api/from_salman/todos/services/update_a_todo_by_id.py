from sqlalchemy.orm import Session

from ..helpers import get_todo
from ..schema import TodoUpdateRequest


def update_a_todo_by_id_(
    todo_id: str,
    body: TodoUpdateRequest,
    db_session: Session,
):

    todo = get_todo(todo_id=todo_id, db_session=db_session)

    todo.title = body.title

    return todo
