from fastapi_utils.cbv import cbv

from main import user_router
from src.api.controllers.user_controller import UserController
from src.api.models.user_models import UserRequest
from src.db.models.user import User


@cbv(user_router)
class UserApi:

    @user_router.get("/user/{_id}")
    def get_user(self, _id: str) -> User:
        return UserController.get_user(_id)

    @user_router.post("/user/")
    def create_user(self, user_request: UserRequest) -> User:
        return UserController.create_user(user_request)

    # @app.get("/users")
    # def get_all_users(self):
    #     return Controllers.get_all_users()
    #
    # @app.get("/users/best")
    # def best_score(self):
    #     user_minScore_document = Controllers.best_score()
    #     # return "user_name" " - " "user_score"
    #     return str(user_minScore_document["user"]) + " - " + str(user_minScore_document["score"])
    #
    # @app.get("/users/scores")
    # def get_all_scores_sorted_by_id(self):
    #     return Controllers.get_all_scores_sorted_by_id()
    #
    # @app.get("/users/{user}?top=3")
    # def get_top3_names_start_with_specific_letter(self, user):
    #     return Controllers.get_top3_names_specific(user)
    #

    #
    # @app.put("/user/{_id}")
    # def update_user(self, _id, user_schema):
    #     return user_schema
    #
    # @app.delete("/user/{_id}")
    # def delete_user(self, _id):
    #     if Controllers.delete_user(_id) == 1:
    #         return _id + "Is deleted"
    #     else:
    #         return "Not deleted, " + _id + "doesn't exists"
