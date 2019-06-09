from gevent import monkey
monkey.patch_all()

import grpc.experimental.gevent as grpc_gevent
grpc_gevent.init_gevent()

import os
import time
from flask import Flask, render_template, request, jsonify
from gevent.pywsgi import WSGIServer

from google.cloud import firestore

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/recentPersons', methods=['GET'])
def get_recent_persons():
    db = firestore.Client()
    persons = db.collection('persons')
    limit = request.args.get('limit')
    try:
        limit = int(limit)
    except (TypeError, ValueError):
        limit = 10

    results = []
    for doc in persons.order_by('created_at', direction='DESCENDING').limit(limit).get():
        doc_dict = doc.to_dict()
        doc_dict['id'] = doc.id
        results.append(doc_dict)
    return jsonify(results)


@app.route('/api/persons', methods=['POST'])
def create_persons():
    db = firestore.Client()
    persons = db.collection('persons')

    body = request.get_json()
    if not body or 'firstname' not in body or 'lastname' not in body:
        err_msg = 'JSON body must contain "firstname" and "lastname"'
        return jsonify({'error': err_msg}), 400

    ts, doc_ref = persons.add({
        u'firstname': body.get('firstname'),
        u'lastname': body.get('lastname'),
        u'created_at': time.time(),
    })
    return jsonify({'id': doc_ref.id})


@app.route('/api/persons/<string:person_id>', methods=['GET'])
def get_person(person_id):
    db = firestore.Client()
    person = db.collection('persons').document(person_id).get()
    if not person.exists:
        err_msg = 'No person with that ID exists'
        return jsonify({'error': err_msg}), 404

    person_dict = person.to_dict()
    person_dict['id'] = person.id
    return jsonify(person_dict)


if __name__ == '__main__':
    server = WSGIServer(('0.0.0.0', int(os.environ.get('PORT', 8080))), app)
    server.serve_forever()
