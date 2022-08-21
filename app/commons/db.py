from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.commons.settings import config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL,
    echo=True,
    future=True,
)

Base = declarative_base()

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    future=True,
)


def get_db():
    session: Session = SessionLocal()
    try:
        with session.begin():
            yield session
    except Exception:
        session.rollback()
    finally:
        session.close()
