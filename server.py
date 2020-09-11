from flask import Flask, request
from datetime import datetime
import time

app = Flask(__name__)

db = []


@app.route("/")
def hello():
    return "Hello, World! <a href='/status'>Status</a>"


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'My Messenger',
        'time': datetime.now().isoformat(),
        'messages': len(db)
    }


@app.route("/send", methods=['POST'])
def send():
    data = request.json
    db.append({
        'id': len(db),
        'name': data['name'],
        'text': data['text'],
        'timestamp': time.time()
    })
    return {'ok': True}


@app.route("/messages")
def messages():
    if 'after_id' in request.args:
        after_id = int(request.args['after_id']) + 1
    else:
        after_id = 0
    return {'messages': db[after_id:]}


app.run()