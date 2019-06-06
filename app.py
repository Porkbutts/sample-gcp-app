from gevent import monkey
monkey.patch_all()

import os
from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer

from db import mongodb

app = Flask(__name__)

@app.route('/')
def index():
    try:
        db = mongodb()
        visitor_ip = request.remote_addr
        db.visitors.update_one({'_id': visitor_ip}, {
            '$inc': {'visit_count': 1}, 
            '$set': {'_id': visitor_ip}
        }, upsert=True)
    except Exception as e:
        print(e)
    return 'Hello, World!'

@app.route('/api/signatures', methods=['GET', 'POST'])
def signatures():
    db = mongodb()
    if request.method == 'POST':
        body = request.get_json()
        rsp = db['signatures'].insert_one({
            'author': body.get('author'),
            'message': body.get('message'),
        })
        return jsonify({
            '_id': str(rsp.inserted_id)
        })
    else:
        return jsonify([{
            '_id': str(x['_id']),
            'author': x['author'],
            'message': x['message'],
        } for x in db['signatures'].find({})])

if __name__ == '__main__':
    server = WSGIServer(('0.0.0.0', int(os.environ.get('PORT', 8080))), app)
    server.serve_forever()
