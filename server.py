from flask import Flask
from datetime import datetime

app = Flask(__name__)


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

app.run()