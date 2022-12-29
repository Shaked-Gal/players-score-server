from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    score: int
