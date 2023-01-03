from src.db.init_db import get_mongo_db_manager
from random import randint


class ScoreControllers:
    mongo_db_manager = get_mongo_db_manager()

    # @classmethod
    # def guess_random(cls, name, number):
    #     # Guess:
    #     random_number = randint(1, 9)
    #     my_score = 0
    #     user_score = 0
    #     while my_score != random_number:
    #         my_score = int(input(f"Guess my secret number from 1 to 9:"))
    #     if my_score < random_number:
    #         print("Incorrect, too low")
    #     elif my_score > random_number:
    #         print("Incorrect, too high")
    #     user_score += 1
    #     print(f" Correct! Good job {user_name}, my secret number is indeed {random_number}\n "
    #           f"You have guessed it in {user_score} guesses.")

    # cls.create_user(cls, user_name, user_score)
    # Function not done

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
