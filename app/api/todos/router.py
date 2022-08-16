from fastapi import APIRouter, Depends, status

from app.commons.dependices import get_db_session

from .schema import TodoCreateRequest, TodoResponse, TodoUpdateRequest
from .services.create_a_todo import create_a_todo_
from .services.delete_a_todo_by_id import delete_a_todo_by_id_
from .services.get_a_todo_by_id import get_a_todo_by_id_
from .services.get_list_of_todos import get_list_of_todos_
from .services.toggle_a_todo_by_id import toggle_a_todo_by_id_
from .services.update_a_todo_by_id import update_a_todo_by_id_

todo_router = APIRouter(prefix="/todo", tags=["todo"])


@todo_router.get("/", response_model=list[TodoResponse])
def get_list_of_todos(db_session=Depends(get_db_session)):
    return get_list_of_todos_(db_session)


@todo_router.post("/", response_model=TodoResponse)
def create_a_todo(
    body: TodoCreateRequest,
    db_session=Depends(get_db_session),
):
    return create_a_todo_(body, db_session)


@todo_router.get("/{todo_id}", response_model=TodoResponse)
def get_a_todo_by_id(
    todo_id: str,
    db_session=Depends(get_db_session),
):
    return get_a_todo_by_id_(todo_id, db_session)


@todo_router.put("/{todo_id}", response_model=TodoResponse)
def update_a_todo_by_id(
    todo_id: str,
    body: TodoUpdateRequest,
    db_session=Depends(get_db_session),
):
    return update_a_todo_by_id_(todo_id, body, db_session)


@todo_router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_a_todo_by_id(
    todo_id: str,
    db_session=Depends(get_db_session),
):
    return delete_a_todo_by_id_(todo_id, db_session)


@todo_router.post("/{todo_id}/toggle", response_model=TodoResponse)
def toggle_a_todo_by_id(
    todo_id: str,
    db_session=Depends(get_db_session),
):
    return toggle_a_todo_by_id_(todo_id, db_session)
