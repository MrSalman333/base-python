from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.api.users.schemas import UserResponse

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    todos = relationship("Item")
    username = Column(String)
    email = Column(String)
    password = Column(String)

    def to_response(self) -> UserResponse:
        return UserResponse(id= self.id, username= self.username, email= self.email)

    def __repr__(self):
       return f"User(id={self.id!r}, username={self.username!r})"


class Item(Base):
     __tablename__ = "items"
     
     id = Column(Integer, primary_key=True)
     name = Column(String)
     user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))


     def __repr__(self):
         return f"Item(id={self.id!r}, name={self.name!r})"
