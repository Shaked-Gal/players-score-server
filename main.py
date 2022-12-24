import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient

from src.dal.mongo_db import MongoDB

app = FastAPI()

# initialize mongo db
db_name = "myDB"
collection_name = "users"
client = MongoClient('localhost', 27017)
db = MongoDB(client, db_name)

if __name__ == '__main__':
    uvicorn.run(app)
