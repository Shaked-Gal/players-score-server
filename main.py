import uvicorn
from pymongo import MongoClient

from src.api.player_api import app
from src.dal.mongo_db import MongoDB

# initialize mongo db
db_name = "myDB"
collection_name = "users"
client = MongoClient('localhost', 27017)
db = MongoDB(client, db_name)

if __name__ == '__main__':
    uvicorn.run(app)
