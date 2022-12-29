from abc import abstractmethod, ABCMeta


class DatabaseManager(metaclass=ABCMeta):
    @abstractmethod
    def insert_one(self, data):
        pass

    @abstractmethod
    def insert_many(self, data_list):
        pass

    @abstractmethod
    def find_one(self, query):
        pass

    @abstractmethod
    def find_many(self, query):
        pass

    @abstractmethod
    def update_one(self, query, update):
        pass

    @abstractmethod
    def update_many(self, query, update):
        pass

    @abstractmethod
    def delete_one(self, query):
        pass

    @abstractmethod
    def delete_many(self, query):
        pass
