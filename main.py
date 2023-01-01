import uvicorn
from fastapi import FastAPI

import src.api.view.user_api as user_api
from config.config import DB_NAME, COLLECTION_NAME
from src.db.mongo_db import MongoDBManager


def get_mongo_db_manager():
    return mongoDBManager


#  todo : needs to happen only once
mongoDBManager = MongoDBManager(DB_NAME, COLLECTION_NAME)
print("---initialized mongo db---")

app = FastAPI()
app.include_router(user_api.router)


@app.get('/')
def home():
    return {
        "message": "we are in home page"
    }


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=3000,
        reload=False,
    )
