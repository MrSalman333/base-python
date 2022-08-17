from sqlalchemy.orm import Session

from ..helpers import get_todo


def get_a_todo_by_id_(
    todo_id: str,
    db_session: Session,
):

    todo = get_todo(todo_id=todo_id, db_session=db_session)

    return todo
