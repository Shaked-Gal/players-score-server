from config.config import DB_NAME, COLLECTION_NAME
from src.db.mongo_db import MongoDBManager

mongoDBManager = MongoDBManager(DB_NAME, COLLECTION_NAME)
print("---initialized mongo db---")


def get_mongo_db_manager():
    return mongoDBManager
