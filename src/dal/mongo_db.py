from pymongo import MongoClient

from src.dal.db import DB


class MongoDB(DB):

    def __init__(self, db_name):
        self.client = MongoClient()
        self.db_name = db_name
        self.db = self.client[db_name]

    def insert_one(self, collection_name, new_record):
        self.db[collection_name].insert_one(new_record)

    def update_one(self):
        pass

    def delete_one(self, collection_name, record_id):
        pass

    def find_by_id(self, collection_name, record_id):
        pass
