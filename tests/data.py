from pydantic import BaseModel


class SeedData(BaseModel):

    users: list[dict] = [
        {"username": "user1", "password": "dsadsa"},
        {"username": "user2", "password": "dsadsa"},
        {"username": "user3", "password": "dsadsa"},
        {"username": "user4", "password": "dsadsa"},
        {"username": "user5", "password": "dsadsa"},
    ]

    users_tokens: list[str] = []
