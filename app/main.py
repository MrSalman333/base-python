# import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.items import routes as items_routes
from app.api.users import routes as users_routes

app = FastAPI(title="Todo App, by salman")

app.include_router(items_routes.router)
app.include_router(users_routes.router)

origins = [
    "http://localhost",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def create_all_tables():
    # NOTE: this is not good at all, it is a temp work around so we don't do the migration set up now
    from sqlalchemy_utils import create_database, database_exists

    from app.commons.db import Base, engine

    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
