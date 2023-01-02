from fastapi import APIRouter
from fastapi_utils.cbv import cbv
from src.api.controllers.score_controllers import ScoreControllers

score_router = APIRouter(tags=["score"])


@cbv(score_router)
class UserApi:
    @score_router.get("/score/guess/{number}")
    def guess(self, number):
        return ScoreControllers.guess_random(number)

    @score_router.get("/score/best")
    def best_score(self):
        return ScoreControllers.best_score()

    @score_router.get("/score/scores")
    def get_all_scores_sorted_by_score(self):
        return ScoreControllers.get_all_scores_sorted_by_score()

    @score_router.get("/score/{user}?top=3")
    def get_top_three_scores_with_specific_name(self, user):
        return ScoreControllers.get_top_three_scores_with_specific_name(user)
