from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Todo


def get_todo(todo_id: str, db_session: Session, user_id: str) -> Todo:
    stmt = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
    todo: Todo | None = db_session.execute(stmt).scalar_one_or_none()

    if todo is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return todo
