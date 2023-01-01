from src.db.init_db import get_mongo_db_manager


class ScoreControllers:
    mongo_db_manager = get_mongo_db_manager()
    pass
    #
    # @classmethod
    # def guess_random(cls):
    #
    #     user_name = str(input(f"Enter your name:"))
    #
    #     # Guess:
    #     random_number = random.randint(1, 9)
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
    #
    #     cls.create_user(cls, user_name, user_score)
    #
    # @classmethod
    # def best_score(cls):
    #     return cls.mongo_db_manager.find_best_score()
    #
    # @classmethod
    # def get_all_users(cls):
    #     return cls.mongo_db_manager.find_all_users()
    #
    # @classmethod
    # def get_all_scores_sorted_by_id(cls):
    #     return cls.mongo_db_manager.find_all_scores_sorted_by_id()
    #
    # @classmethod
    # def get_top_three_names_specific(cls, user):
    #     return cls.mongo_db_manager.find_top_three_names_specific(user)
    #

    # @classmethod
    # def delete_user(cls, user_id):
    #     if user_id == cls.mongo_db_manager.find_by_id(user_id)["_id"]:
    #         cls.mongo_db_manager.delete_one(user_id)
    #         return 1
    #     else:
    #         return 0
