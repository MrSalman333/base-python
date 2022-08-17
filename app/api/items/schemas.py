from pydantic import BaseModel

class ItemResponse(BaseModel):
    id: int
    name: str

class ItemRequest(BaseModel):
    name: str