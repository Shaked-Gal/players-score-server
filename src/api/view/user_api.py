from fastapi import APIRouter, Body

from src.api.controllers.user_controllers import UserControllers
from src.api.models.models import UserRequest
from src.db.models.user import User
from fastapi_utils.cbv import cbv

user_router = APIRouter(tags=["user"])


@cbv(user_router)
class UserApi:
    @user_router.get("/user/{_id}")
    def get_user(self, _id) -> User:
        return UserControllers.get_user(_id)

    @user_router.post("/user/")
    def create_user(self, user_request: UserRequest = Body(..., example={
        "user": "Tom",
        "score": 3
    })):
        return UserControllers.create_user(user_request)

    @user_router.get("/user")
    def get_all_users(self):
        return UserControllers.get_all_users()

    @user_router.put("/user/{_id}")
    def update_user(self, _id, user_request: UserRequest = Body(..., example={
        "user": "Tom",
        "score": 3
    })):
        return UserControllers.update_user(_id, user_request)

    @user_router.delete("/user/{_id}")
    def delete_user(self, _id):
        return UserControllers.delete_user(_id)
