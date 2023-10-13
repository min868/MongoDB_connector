import pymongo
from pymongo import errors


class MongoDB:
    def __init__(self, db_url, db_name):
        self.url = db_url
        self.db = db_name
        self.connect()

    def connect(self):
        self._connect()

    def _connect(self):
        try:
            connection = pymongo.MongoClient(self.url)
            self.database = connection[self.db]
        except pymongo.errors.ConnectionFailure as e:
            print(f"Connection to MongoDB failed due to: {str(e)}")

    def get_database(self):
        return self.database


CONNECTOR = MongoDB('mongodb://localhost:27017', 'CRUDjango')
DB = CONNECTOR.get_database()
