import re
from typing import Union
from uuid import UUID

from pydantic import BaseModel, validator


class UserResponse(BaseModel):
     id: UUID
     username: str
    

class UserRequest(BaseModel):
     username: str
     password: str
     
     @validator("username")
     def validate_username(cls, username):
          if not username:
               raise AssertionError("no Username was provided")
          
          if len(username) < 5 or len(username) > 20:
               raise AssertionError("Username must be between 5 and 20 characters") 
          
          return username 
     
     @validator("password")
     def validate_password(cls, password):
          if not password:
               raise AssertionError("no Password was provided")
          
          return password
     

class TokenData(BaseModel):
    username: Union[str, None] = None
