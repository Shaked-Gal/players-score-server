from bson import ObjectId
from pydantic import BaseModel


class User(BaseModel):
    _id: ObjectId
    user: str
    score: int
