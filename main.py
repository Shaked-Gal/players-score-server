import uvicorn
from fastapi import FastAPI, APIRouter

from config.config import DB_NAME, COLLECTION_NAME
from src.db.mongo_db import MongoDBManager


def get_mongo_db_manager():
    return mongoDBManager


#  todo : needs to happen only once
mongoDBManager = MongoDBManager(DB_NAME, COLLECTION_NAME)
print("---initialized mongo db---")

app = FastAPI()
user_router = APIRouter(tags=["user"])

app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=3000,
        reload=False,
    )
