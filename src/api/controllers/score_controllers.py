from src.db.init_db import get_mongo_db_manager
from src.api.models.models import User, SortOrder
from typing import Union


class ScoreControllers:
    mongo_db_manager = get_mongo_db_manager()

    @classmethod
    def best_score(cls) -> Union[User, str]:
        # Best score is the lowest number (the least guesses)
        try:
            sort_order_asc = 1
            user_db = cls.mongo_db_manager.find_many({}).sort([("score", sort_order_asc)])[0]
            return User(id=str(user_db["_id"]), user=user_db["user"], score=user_db["score"])
        except IndexError:
            return "IndexError: There are no users in the collection"

    @classmethod
    def get_all_scores_sorted_by_score(cls, sort_order: SortOrder) -> Union[list, str]:
        try:
            length = cls.mongo_db_manager.collection.count_documents({})
            if length == 0:
                return "There are no users in the collection"
            sort_order_asc = 1
            if sort_order == SortOrder.DESC:
                sort_order_asc = -1
            users = cls.mongo_db_manager.find_many({}).sort([("score", sort_order_asc)])
            users_list = []
            for user in users:
                users_list.append(User(id=str(user["_id"]), user=user["user"], score=user["score"]))
            return users_list
        except Exception as err:
            return str(err)

    @classmethod
    def get_top_scores_by_count(cls, count: int) -> Union[list, str]:
        try:
            length = cls.mongo_db_manager.collection.count_documents({})
            if length == 0:
                return "There are no users in the collection"
            sort_order_asc = 1
            users = cls.mongo_db_manager.find_many({}).sort([("score", sort_order_asc)]).limit(count)
            users_list = []
            for user in users:
                users_list.append(User(id=str(user["_id"]), user=user["user"], score=user["score"]))
            return users_list
        except Exception as err:
            return str(err)
