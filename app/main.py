from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.api.auth.router import auth_router
from app.api.todos.router import todo_router
from app.api.users.router import user_router
from app.commons.settings import config

app = FastAPI(title="Todo App")
# app.include_router(todo_router)
# app.include_router(user_router)
app.include_router(auth_router)

app.add_middleware(CORSMiddleware, allow_origins=config.ALLOWED_CORS_ORIGINS)
app.add_middleware(GZipMiddleware)


@app.on_event("startup")
def create_all_tables():
    # NOTE: this is not good at all ,, it is a temp work around so we don't do the migration set up now
    from sqlalchemy_utils import create_database, database_exists

    from app.commons.database import Base, engine

    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
