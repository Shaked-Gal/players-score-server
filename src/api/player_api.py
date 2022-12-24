from fastapi import FastAPI

from src.controllers.controllers import Controllers

app = FastAPI()

controller = Controllers()


class UserApi:

    @app.get("/user/{_id}")
    def get_user(self, _id):
        return Controllers.get_user(controller, _id)

    @app.get("/users")
    def get_all_users(self):
        return Controllers.get_all_users(controller)

    @app.get("/users/best")
    def best_score(self):
        user_minScore_document = Controllers.best_score(controller)

        # return "user_name" " - " "user_score"
        return str(user_minScore_document["user"]) + " - " + str(user_minScore_document["score"])

    @app.get("/users/scores")
    def get_all_scores_sorted_by_id(self):
        return Controllers.get_all_scores_sorted_by_id(controller)

    @app.get("/users/{user}?top=3")
    def get_top3_names_start_with_specific_letter(self, user):
        return Controllers.get_top3_names_specific(controller, user)

    @app.post("/user/")
    def create_user(self, user_schema):
        Controllers.create_user(controller, user_schema["user"], user_schema["score"])
        return user_schema

    @app.put("/user/{_id}")
    def update_user(self, _id, user_schema):
        return user_schema

    @app.delete("/user/{_id}")
    def delete_user(self, _id):
        if Controllers.delete_user(controller, _id) == 1:
            return _id + "Is deleted"
        else:
            return "Not deleted, " + _id + "doesn't exists"
