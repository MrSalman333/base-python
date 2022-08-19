from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import Todo


def get_list_of_todos_(
    db_session: Session,
):

    stmt = select(Todo).order_by(Todo.created_at.desc())
    todos: list[Todo] = db_session.execute(stmt).scalars().all()
    return todos
