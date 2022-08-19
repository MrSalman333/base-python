import re
from typing import Union
from uuid import UUID

from pydantic import BaseModel, validator


class UserResponse(BaseModel):
     id: UUID
     username: str
     email: str
    

class UserRequest(BaseModel):
     username: str
     # email: str
     password: str
     
     @validator("username")
     def validate_username(cls, username):
          if not username:
               raise AssertionError("no Username was provided")
          
          if len(username) < 5 or len(username) > 20:
               raise AssertionError("Username must be between 5 and 20 characters") 
          
          return username 
     
     # @validator("email")
     # def validate_email(cls, email):
     #      if not email:
     #           raise AssertionError("no Email was provided")
          
     #      if not re.match("[^@]+@[^@]+\.[^@]+", email):
     #           raise AssertionError("Provided email is not an email address") 
          
     #      return email
     
     @validator("password")
     def validate_password(cls, password):
          if not password:
               raise AssertionError("no Password was provided")
          
          return password
     

class TokenData(BaseModel):
    email: Union[str, None] = None
