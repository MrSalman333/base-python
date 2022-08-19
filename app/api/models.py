from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declarative_base, relationship

from app.api.users.schemas import UserResponse
from app.commons.db import Base

Base = declarative_base()

class Item(Base):
     __tablename__ = "items"
     
     id: int = Column(Integer, primary_key=True)
     name: str = Column(String)
     user_id: str = Column(String, ForeignKey("users.id"))


     def __repr__(self):
         return f"Item(id={self.id!r}, name={self.name!r})"


class User(Base):
    __tablename__ = "users"

    id: str = Column(String, primary_key=True, default=lambda: str(uuid4()))
    todos: Mapped[int] = relationship("Item")
    username: str = Column(String)
    password: str = Column(String)

    def to_response(self) -> UserResponse:
        return UserResponse(id= self.id, username= self.username)

    def __repr__(self):
       return f"User(id={self.id!r}, username={self.username!r})"
