import os

MONGODB_CONNECTION_STRING = os.environ.get('MONGODB_CONNECTION_STRING', 'localhost')
MONGODB_DATABASE = os.environ.get('MONGODB_DATABASE', 'test')
