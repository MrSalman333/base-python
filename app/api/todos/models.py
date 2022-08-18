from datetime import datetime
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.orm import Mapped

from app.commons.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[str] = sa.Column(sa.String, primary_key=True, default=lambda: str(uuid4()))  # type: ignore
    created_at: Mapped[datetime] = sa.Column(sa.DateTime, nullable=False, default=datetime.now)  # type: ignore
    title: Mapped[str] = sa.Column(sa.String, nullable=False)  # type: ignore
    is_chceked: Mapped[bool] = sa.Column(sa.Boolean, nullable=False, default=False)  # type: ignore
    user_id: Mapped[str] = sa.Column(sa.ForeignKey("users.id"), nullable=False, index=True)  # type: ignore
