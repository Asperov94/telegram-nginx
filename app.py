# -*- coding: utf-8 -*-
"""send message to telegram via nginx"""
import requests
import yaml
from flask import Flask, request, abort, jsonify

def telegram(text, bot):
    """ Send message func """
    url = "https://api.telegram.org/bot" + bot + "/sendMessage"
    data = {"chat_id" : config["chat_id"], "text" : text}
    response = requests.post( url, json=data)

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile)

app = Flask(__name__)

@app.route('/' + config["url"], methods=['POST'])
def handle_push():
    """push message to nginx"""
    if not request.json:
        abort(400)
    telegram(request.json.get('text'), config["bot"])
    return jsonify ({'status': 'ok'}) , 200

if __name__ == '__main__':
    print("Listening...")
    app.run(host=config["host"], port=config["port"])