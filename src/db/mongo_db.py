from pymongo import MongoClient

from src.db.db import DatabaseManager


class MongoDBManager(DatabaseManager):
    def __init__(self, db_name: str, collection_name: str):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, data):
        return self.collection.insert_one(data)

    def insert_many(self, data_list):
        return self.collection.insert_many(data_list)

    def find_one(self, query):
        return self.collection.find_one(query)

    def find_many(self, query):
        return self.collection.find(query)

    def update_one(self, query, update):
        return self.collection.update_one(query, update)

    def update_many(self, query, update):
        return self.collection.update_many(query, update)

    def delete_one(self, query):
        return self.collection.delete_one(query)

    def delete_many(self, query):
        return self.collection.delete_many(query)
