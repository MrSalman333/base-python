from fastapi import APIRouter, Depends, status

from app.commons.dependices import get_db_session, get_verified_current_user_or_none, login_required

from .schema import TodoCreateRequest, TodoResponse, TodoUpdateRequest
from .services.create_a_todo import create_a_todo_
from .services.delete_a_todo_by_id import delete_a_todo_by_id_
from .services.get_a_todo_by_id import get_a_todo_by_id_
from .services.get_list_of_todos import get_list_of_todos_
from .services.toggle_a_todo_by_id import toggle_a_todo_by_id_
from .services.update_a_todo_by_id import update_a_todo_by_id_

todo_router = APIRouter(prefix="/todo", tags=["todo"])


@todo_router.get("", response_model=list[TodoResponse], dependencies=[Depends(login_required)])
def get_list_of_todos(
    db_session=Depends(get_db_session),
    current_user=Depends(get_verified_current_user_or_none),
):
    return get_list_of_todos_(db_session, current_user)


@todo_router.post("", response_model=TodoResponse, dependencies=[Depends(login_required)])
def create_a_todo(
    body: TodoCreateRequest,
    db_session=Depends(get_db_session),
    current_user=Depends(get_verified_current_user_or_none),
):
    return create_a_todo_(body, db_session, current_user)


@todo_router.get("/{todo_id}", response_model=TodoResponse, dependencies=[Depends(login_required)])
def get_a_todo_by_id(
    todo_id: str,
    db_session=Depends(get_db_session),
    current_user=Depends(get_verified_current_user_or_none),
):
    return get_a_todo_by_id_(todo_id, db_session, current_user)


@todo_router.put("/{todo_id}", response_model=TodoResponse, dependencies=[Depends(login_required)])
def update_a_todo_by_id(
    todo_id: str,
    body: TodoUpdateRequest,
    db_session=Depends(get_db_session),
    current_user=Depends(get_verified_current_user_or_none),
):
    return update_a_todo_by_id_(todo_id, body, db_session, current_user)


@todo_router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(login_required)])
def delete_a_todo_by_id(
    todo_id: str,
    db_session=Depends(get_db_session),
    current_user=Depends(get_verified_current_user_or_none),
):
    return delete_a_todo_by_id_(todo_id, db_session, current_user)


@todo_router.post("/{todo_id}/toggle", response_model=TodoResponse, dependencies=[Depends(login_required)])
def toggle_a_todo_by_id(
    todo_id: str,
    db_session=Depends(get_db_session),
    current_user=Depends(get_verified_current_user_or_none),
):
    return toggle_a_todo_by_id_(todo_id, db_session, current_user)
