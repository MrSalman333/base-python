import os
from functools import lru_cache

from pydantic import BaseSettings


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


config.DB_NAME
config.SQLALCHEMY_DATABASE_URL
