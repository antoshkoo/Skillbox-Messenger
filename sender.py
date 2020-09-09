import requests

url = 'http://127.0.0.1:5000/send'

data = {
    'name': 'Jack',
    'text': 'text'
}

responce = requests.post(url, json=data)