# import sys

# sys.path.append("...")
import os
from functools import lru_cache

from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


class BaseConfig(BaseSettings):
    # this is for auto complate
    production: bool = False
    testing: bool = False
    # the current stage
    ENVIRONMENT: str = "default"
    APP_NAME: str = "todo"

    # the allowed browser sites requests
    ALLOWED_CORS_ORIGINS = ["*"]
    ALLOWED_HOSTS: list[str] = ["*"]

    # db configs
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int

    # generate SQLALCHEMY_DATABASE_URL dynamically
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    AUTH_SALT: str
    AUTH_JWT_KEY: str
    AUTH_TOKEN_EXPIRE_IN: int = 600
    AUTH_REFRESH_TOKEN_EXPIRE_IN: int = 1000
    ALGORITHM: str


class ProductionConfig(BaseSettings):
    production = True
    testing = False
    ENVIRONMENT = "prod"


class StagingConfig(BaseSettings):
    production = True
    testing = False
    ENVIRONMENT = "staging"


class TestingConfig(BaseSettings):
    production = False
    testing = True
    ENVIRONMENT = "testing"


@lru_cache()
def current_config():
    """
    this will load the required config passed on STAGE env if not set it will load LocalConfig
    """
    stage = os.environ.get("ENVIRONMENT", "local")

    if stage == "prod":
        config = ProductionConfig()
    elif stage == "staging":
        config = StagingConfig()
    elif stage == "testing":
        config = TestingConfig()
    elif stage == "local":
        config = BaseConfig()
    else:
        raise Exception(f"ENVIRONMENT: {stage} is not supported")

    return config


config = current_config()


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
