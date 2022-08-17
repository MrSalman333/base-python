import uuid

from fastapi import HTTPException
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

from app.api.users.schemas import UserResponse

Base = declarative_base()

class Item(Base):
     __tablename__ = "items"

     id = Column(Integer, primary_key=True)
     name = Column(String)

     def __repr__(self):
         return f"Item(id={self.id!r}, name={self.name!r})"


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String)
    email = Column(String)
    password = Column(String)

     
    def to_response(self) -> UserResponse:
        return UserResponse(id= self.id, username= self.username, email= self.email)
    
    def __repr__(self):
       return f"User(id={self.id!r}, username={self.username!r})"
