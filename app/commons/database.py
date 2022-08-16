from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.commons.settings import config

engine = create_engine(url=config.SQLALCHEMY_DATABASE_URL)

# following https://fastapi.tiangolo.com/tutorial/sql-databases
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)

Base = declarative_base()
