from gevent import monkey
monkey.patch_all()
from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    server = WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()