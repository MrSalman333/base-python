from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.commons.settings import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
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
