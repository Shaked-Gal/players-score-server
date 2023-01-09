from enum import Enum

from pydantic import BaseModel


class UserRequest(BaseModel):
    user: str
    score: int


class User(BaseModel):
    id: str
    user: str
    score: int


class SortOrder(str, Enum):
    ASC = 'asc'
    DESC = 'desc'
