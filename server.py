from time import time
from tokenize import Token
from flask import Flask, request
from message import Message
import requests

PORT = 8080

TOKEN = ""
API_URL = f"https://api.telegram.org/bot{TOKEN}" + "/{method_name}"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main(*args, **kwargs):
    message = Message(request.json['message'], Token)
    method_name, params = message.get_response()
    while not send_response(method_name, params):
        time.sleep(5)
    return "ok"

def send_response(method_name, params):
    r = requests.post(url=API_URL.format(method_name=method_name), params=params)
    return r.status_code == 200

@app.route('/.well-known/acme-challenge/<challenge>')
def verify_challenge(challenge):
    challenge_file = open('.well-known/acme-challenge/' + challenge)
    return challenge_file.read()

if __name__ == '__main__':
    app.run('0.0.0.0', port=PORT)