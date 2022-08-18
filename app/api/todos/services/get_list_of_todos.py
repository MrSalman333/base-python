from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import Todo


def get_list_of_todos_(
    db_session: Session,
    current_user: dict,
):

    stmt = select(Todo).where(Todo.user_id == current_user["sub"]).order_by(Todo.created_at.desc())
    todos: list[Todo] = db_session.execute(stmt).scalars().all()
    return todos
