from src.db.init_db import get_mongo_db_manager
from random import randint


class ScoreControllers:
    mongo_db_manager = get_mongo_db_manager()

    @classmethod
    def best_score(cls):
        # Best score is the lowest number (the least guesses)
        return str(cls.mongo_db_manager.find_many({}).sort([("score", 1)]).limit(1)[0])

    @classmethod
    def get_all_scores_sorted_by_score_ascending(cls):
        users = cls.mongo_db_manager.find_many({}).sort([("score", 1)])
        if users is None:
            return {"error": "Users not found"}
        length = cls.mongo_db_manager.collection.count_documents({})
        users_list = [next(users) for _ in range(length)]
        return str(users_list)

    @classmethod
    def get_top_three_scores_with_specific_name(cls, user: str):
        # Top scores are the least guesses (the lowest numbers)
        users = cls.mongo_db_manager.find_many({"user": user}).sort([("score", 1)]).limit(3)
        if users is None:
            return {"error": "Users not found"}
        top_three_documents = []
        for document in users:
            top_three_documents.append(document)
        return str(top_three_documents)
