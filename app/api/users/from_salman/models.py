from datetime import datetime
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.orm import Mapped

from app.commons.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = sa.Column(sa.String, primary_key=True, default=lambda: str(uuid4()))  # type: ignore
    created_at: Mapped[datetime] = sa.Column(sa.DateTime, nullable=False, default=datetime.now)  # type: ignore
    username: Mapped[str] = sa.Column(sa.String, nullable=False, unique=True)  # type: ignore
    hashed_password: Mapped[str] = sa.Column(sa.String, nullable=False)  # type: ignore
