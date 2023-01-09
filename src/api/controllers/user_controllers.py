from typing import Union

from bson.errors import InvalidId
from src.api.models.models import UserRequest, User
from src.db.init_db import get_mongo_db_manager
from bson import ObjectId


class UserControllers:
    mongo_db_manager = get_mongo_db_manager()

    @classmethod
    def get_user(cls, user_id: str) -> Union[User, str]:
        try:
            user_obj_id = ObjectId(user_id)
            user_db = cls.mongo_db_manager.find_one({"_id": user_obj_id})
            if user_db is None:
                return "User not found"
            return User(id=user_id, user=user_db["user"], score=user_db["score"])
        except InvalidId as err:
            return str(err)

    @classmethod
    def create_user(cls, user_request: UserRequest) -> Union[User, str]:
        try:
            my_filter = {"user": user_request.user, "score": user_request.score}
            user_db_id = str(cls.mongo_db_manager.insert_one(my_filter).inserted_id)
            return User(id=user_db_id, user=user_request.user, score=user_request.score)
        except Exception as err:
            return str(err)

    @classmethod
    def get_all_users(cls) -> Union[list, str]:
        try:
            users = cls.mongo_db_manager.find_many({})
            if users is None:
                return "There are no users in the collection"
            users_list = []
            for user in users:
                users_list.append(User(id=str(user["_id"]), user=user["user"], score=user["score"]))
            return users_list
        except Exception as err:
            return str(err)

    @classmethod
    def update_user(cls, _id: ObjectId, user_request: UserRequest) -> str:
        try:
            user_obj_id = ObjectId(_id)
            user_db = cls.mongo_db_manager.find_one({"_id": user_obj_id})
            if user_db is None:
                return "User not found"
            my_filter = {"_id": user_obj_id}
            my_new_values = {"$set": {"user": user_request.user, "score": user_request.score}}
            cls.mongo_db_manager.update_one(my_filter, my_new_values)
            return "User updated"
        except InvalidId as err:
            return str(err)

    @classmethod
    def delete_user(cls, _id) -> str:
        try:
            user_obj_id = ObjectId(_id)
            user = cls.mongo_db_manager.find_one({"_id": user_obj_id})
            if user is None:
                return "User not found"
            cls.mongo_db_manager.delete_one({"_id": user_obj_id})
            return "User deleted"
        except InvalidId as err:
            return str(err)

