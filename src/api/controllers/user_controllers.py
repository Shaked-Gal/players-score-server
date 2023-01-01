from src.api.models.user_models import UserRequest
from src.db.init_db import get_mongo_db_manager


class UserController:
    mongo_db_manager = get_mongo_db_manager()

    @classmethod
    def get_user(cls, user_id: str):
        user = cls.mongo_db_manager.find_one({"user": user_id})
        if user is None:
            return {"error": "User not found"}
        return user

    @classmethod
    def create_user(cls, user_request: UserRequest):
        return cls.mongo_db_manager.insert_one(user_request)
