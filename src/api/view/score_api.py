from fastapi import APIRouter
from fastapi_utils.cbv import cbv
from src.api.controllers.score_controllers import ScoreControllers
from src.api.models.models import SortOrder

score_router = APIRouter(tags=["score"])


@cbv(score_router)
class UserApi:

    @score_router.get("/best-score")
    def best_score(self):
        return ScoreControllers.best_score()

    @score_router.get("/scores")
    def get_all_scores_sorted_by_score(self, sort_order: SortOrder):
        return ScoreControllers.get_all_scores_sorted_by_score(sort_order)

    @score_router.get("/top-scores")
    def get_top_scores_by_count(self, count: int = 3):
        return ScoreControllers.get_top_scores_by_count(count)
