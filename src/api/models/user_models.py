from pydantic import BaseModel


class UserRequest(BaseModel):
    user: str
    score: int
