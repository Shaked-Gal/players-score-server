import random

from main import db, collection_name


class Controllers:

    def guess_random(self):

        user_name = str(input(f"Enter your name:"))

        # Guess:
        random_number = random.randint(1, 9)
        my_score = 0
        user_score = 0
        while my_score != random_number:
            my_score = int(input(f"Guess my secret number from 1 to 9:"))
        if my_score < random_number:
            print("Incorrect, too low")
        elif my_score > random_number:
            print("Incorrect, too high")
        user_score += 1
        print(f" Correct! Good job {user_name}, my secret number is indeed {random_number}\n "
              f"You have guessed it in {user_score} guesses.")

        Controllers.create_user(self, user_name, user_score)

    def best_score(self):
        return db.find_best_score(collection_name)

    def get_user(self, user_id):
        return db.find_by_id(collection_name, user_id)

    def get_all_users(self):
        return db.find_all_users(collection_name)

    def get_all_scores_sorted_by_id(self):
        return db.find_all_scores_sorted_by_id(collection_name)

    def get_top3_names_specific(self, user):
        return db.find_top3_names_specific(collection_name, user)

    def create_user(self, user_name, user_score):
        new_user_data = {'user': user_name, 'score': user_score}
        db.insert_one(collection_name, new_user_data)

    def delete_user(self, user_id):
        if user_id == db.find_by_id(collection_name, user_id)["_id"]:
            db.delete_one(collection_name, user_id)
            return 1
        else:
            return 0
