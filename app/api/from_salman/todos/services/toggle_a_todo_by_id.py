from sqlalchemy.orm import Session

from ..helpers import get_todo


def toggle_a_todo_by_id_(
    todo_id: str,
    db_session: Session,
):
    todo = get_todo(todo_id=todo_id, db_session=db_session)

    todo.is_chceked = not todo.is_chceked

    return todo
