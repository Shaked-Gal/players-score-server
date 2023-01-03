from fastapi import APIRouter
from fastapi_utils.cbv import cbv
from src.api.controllers.score_controllers import ScoreControllers

score_router = APIRouter(tags=["score"])


@cbv(score_router)
class UserApi:

    @score_router.get("/score/best")
    def best_score(self):
        return ScoreControllers.best_score()

    @score_router.get("/score/scores")
    def get_all_scores_sorted_by_score_ascending(self):
        return ScoreControllers.get_all_scores_sorted_by_score_ascending()

    @score_router.get("/score/{user}")
    def get_top_three_scores_with_specific_name(self, user):
        return ScoreControllers.get_top_three_scores_with_specific_name(user)
