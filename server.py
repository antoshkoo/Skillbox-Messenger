from flask import Flask, request
from datetime import datetime

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
        'time': datetime.now().isoformat()
    }


@app.route("/send", methods=['POST'])
def send():
    data = request.json
    db.append({
        'name': data['name'],
        'text': data['text'],
        'timestamp': datetime.now()
    })
    return {'ok': True}


@app.route("/messages")
def messages():
    return {'messages': db}


app.run()