from abc import ABC, abstractmethod


class DB(ABC):

    def __init__(self, client, db_name):
        self.client = client
        self.db_name = db_name
        self.db = self.client[db_name]

    @abstractmethod
    def insert_one(self, collection_name, user_schema):
        raise NotImplementedError()

    @abstractmethod
    def update_one(self, collection_name, user_schema, user_new_schema):
        raise NotImplementedError()

    @abstractmethod
    def delete_one(self, collection_name, user_id):
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, collection_name, user_id):
        raise NotImplementedError()
