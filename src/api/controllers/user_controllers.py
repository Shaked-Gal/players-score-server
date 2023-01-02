from src.api.models.user_models import UserRequest
from src.db.init_db import get_mongo_db_manager
from bson import ObjectId


class UserControllers:
    mongo_db_manager = get_mongo_db_manager()

    @classmethod
    def get_user(cls, user_id):
        user = cls.mongo_db_manager.find_one({"_id": ObjectId(user_id)})
        if user is None:
            return {"error": "User not found"}
        return str(user)

    @classmethod
    def create_user(cls, user_request: UserRequest):
        my_filter = {"user": user_request.user, "score": user_request.score}
        return "User Created, ID: " + str(cls.mongo_db_manager.insert_one(my_filter).inserted_id)

    @classmethod
    def get_all_users(cls):
        users = cls.mongo_db_manager.find_many({})
        if users is None:
            return {"error": "Users not found"}
        length = cls.mongo_db_manager.collection.count_documents({})
        users_list = [next(users) for _ in range(length)]
        return str(users_list)

    @classmethod
    def update_user(cls, _id, user_request: UserRequest):
        my_filter = {"_id": ObjectId(_id)}
        my_new_values = {"$set": {"user": user_request.user, "score": user_request.score}}
        cls.mongo_db_manager.update_one(my_filter, my_new_values)
        return "User updated, updated info: " + str(cls.get_user(_id))

    @classmethod
    def delete_user(cls, _id):
        cls.mongo_db_manager.delete_one({"_id": ObjectId(_id)})
        return "User deleted"
