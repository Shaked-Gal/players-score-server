from fastapi import FastAPI

app = FastAPI()


class PlayerApi:
    # @app.get("/bestScore")
    # def bestScore():
    #     minScore = 0  # Default best score
    #     # todo : use controller functions not db directly
    #     player = data.myCollection.find_one(
    #         sort=[("guesses", 1)])  # Sort guesses and get the first item(ascending order)
    #     return str(player["player"]) + " - " + str(player["guesses"])

    @app.delete("/delete/{id}")
    def deletePlayer(player):
        # player = to be deleted

        myQuery = {"player": player}

        # If there is a player with this name
        if data.myCollection.count_documents(myQuery) != 0:  # Then:
            data.myCollection.delete_one(myQuery)  # Delete
            return player + " Is deleted"
        else:
            return "Not deleted, player doesn't exist"
