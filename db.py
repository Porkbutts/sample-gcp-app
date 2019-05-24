from pymongo import MongoClient

from environment import (MONGODB_DATABASE, MONGODB_USERNAME, MONGODB_PASSWORD,
    MONGODB_HOST, MONGODB_PORT, MONGODB_USE_SRV)


def mongodb():
    conn_string = 'mongodb'
    if MONGODB_USE_SRV:
        conn_string += '+srv'
    conn_string += '://'
    if MONGODB_USERNAME and MONGODB_PASSWORD:
        conn_string += '{}:{}@'.format(MONGODB_USERNAME, MONGODB_PASSWORD)
    conn_string += MONGODB_HOST
    if not MONGODB_USE_SRV:
        conn_string += ':{}'.format(MONGODB_PORT)
    return MongoClient(conn_string)[MONGODB_DATABASE]
