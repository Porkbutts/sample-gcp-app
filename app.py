from gevent import monkey
monkey.patch_all()

import os
from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    server = WSGIServer(('0.0.0.0', os.environ.get('PORT', 8080)), app)
    server.serve_forever()