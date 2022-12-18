from abc import ABC, abstractmethod


class DB(ABC):

    def __init__(self, client, db_name):
        self.client = client
        self.db_name = db_name
        self.db = self.client[db_name]

    @abstractmethod
    def insert_one(self, collection_name, new_record):
        raise NotImplementedError()

    @abstractmethod
    def update_one(self):
        raise NotImplementedError()

    @abstractmethod
    def delete_one(self, collection_name, record_id):
        raise NotImplementedError()
