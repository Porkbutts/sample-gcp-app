import os

MONGODB_DATABASE = os.environ.get('MONGODB_DATABASE', 'sample_gcp_app_local')
MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME')
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')
MONGODB_HOST = os.environ.get('MONGODB_HOST', 'localhost')
MONGODB_PORT = os.environ.get('MONGODB_PORT', 27017)
MONGODB_USE_SRV = os.environ.get('MONGODB_USE_SRV') in ('true', '1')
