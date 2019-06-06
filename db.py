from pymongo import MongoClient

from environment import MONGODB_CONNECTION_STRING, MONGODB_DATABASE

def mongodb():
    return MongoClient(MONGODB_CONNECTION_STRING)[MONGODB_DATABASE]
