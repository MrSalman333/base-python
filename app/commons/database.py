from importlib import import_module

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.commons.settings import config

engine = create_engine(
    url=config.SQLALCHEMY_DATABASE_URL,
    future=True,
)

# following https://fastapi.tiangolo.com/tutorial/sql-databases
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    future=True,
)

Base = declarative_base()

# this is a way to control the import of sqla models
# we do this to achive 2 things
# 1- control the order of the imports
# 2- make sure all needed models have been imported
APP_MODELS = [
    "app.api.todos.models",
    "app.api.users.models",
]

for model in APP_MODELS:
    import_module(model)
