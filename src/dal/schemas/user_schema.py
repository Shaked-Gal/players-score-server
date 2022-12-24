from bson import ObjectId
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    _id: ObjectId
    name: str = Field(example="John")
    score: int = Field(default=0, example=3)

    class Config:
        schema_extra = {
            "example": {
                "_id": "1a2b3c154f387n6837",
                "name": "John",
                "score": 3
            }
        }
