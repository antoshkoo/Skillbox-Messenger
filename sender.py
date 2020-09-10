import requests

url = 'http://127.0.0.1:5000/send'

name = input('Имя: ')
while True:
    text = input('Сообщение:')
    data = {'name': name, 'text': text}
    responce = requests.post(url, json=data)
