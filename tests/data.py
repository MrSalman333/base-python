from typing import Dict, List

from pydantic import BaseModel


class SeedData(BaseModel):

    users: List[Dict] = [
        {"username": "user1", "password": "dsa"},
        {"username": "user2", "password": "dsa"},
        {"username": "user3", "password": "dsa"},
        {"username": "user4", "password": "dsa"},
        {"username": "user5", "password": "dsa"},
    ]

    users_tokens: List[str] = []
