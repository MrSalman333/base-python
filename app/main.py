from fastapi import FastAPI

from app.api.todos.router import todo_router
from app.api.users.router import user_router

app = FastAPI(title="Todo App")
app.include_router(todo_router)
app.include_router(user_router)


@app.on_event("startup")
def create_all_tables():
    # NOTE: this is not good at all ,, it is a temp work around so we don't do the migration set up now
    from sqlalchemy_utils import create_database, database_exists

    from app.commons.database import Base, engine

    if not database_exists(engine.url):
        create_database(engine.url)

    from app.api.todos import models  # noqa
    from app.api.users import models  # noqa

    Base.metadata.create_all(engine)
