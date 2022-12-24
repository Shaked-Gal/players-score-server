from src.dal.db import DB


class MongoDB(DB):

    def __init__(self, client, db_name):
        super().__init__(client, db_name)
        self.client = client
        self.db_name = db_name
        self.db = self.client[db_name]

    def insert_one(self, collection_name, user_schema):
        self.db[collection_name].insert_one(user_schema)

    def update_one(self, collection_name, user_schema, user_new_schema):
        self.db[collection_name].update_one(user_schema, user_new_schema)

    def delete_one(self, collection_name, user_id):
        self.db[collection_name].delete_one(user_id)

    def find_by_id(self, collection_name, user_id):
        return self.db[collection_name].find_one({"_id": user_id})

    def find_all_users(self, collection_name):
        return self.db[collection_name].find()

    def find_best_score(self, collection_name):
        # Get min score(the fewest guesses): Sort guesses(ascending order) and get the first item:
        return self.db[collection_name].find_one(sort=[("score", 1)])

    def find_all_scores_sorted_by_id(self, collection_name):
        return self.db[collection_name].find(sort=["_id"])

    def find_top3_names_specific(self, collection_name, user):
        return self.db[collection_name].find({"user": user}).limit(3)
