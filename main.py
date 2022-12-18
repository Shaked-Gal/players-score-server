import random

from src.dal.mongo_db import MongoDB


def guess_random():
    # Player name:
    player = str(input(f"Enter your name:"))

    # Guess:
    random_number = random.randint(1, 9)
    my_guess = 0
    guesses = 0
    while my_guess != random_number:
        my_guess = int(input(f"Guess my secret number from 1 to 9:"))
        if my_guess < random_number:
            print("Incorrect, too low")
        elif my_guess > random_number:
            print("Incorrect, too high")
        guesses += 1
    print(f" Correct! Good job {player}, my secret number is indeed {random_number}\n "
          f"You have guessed it in {guesses} guesses.")

    # Save player score to db:
    new_player_data = {'player': player, 'guesses': guesses}
    db_name = "myDB"
    collection_name = "players"
    db = MongoDB(db_name)
    db.insert_one(collection_name, new_player_data)


if __name__ == '__main__':
    # todo : run server with uvicorn
    # guess_random()
    print("Game over")
