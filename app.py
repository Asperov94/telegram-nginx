from flask import Flask, request, abort, jsonify
import requests
import json
import yaml

#---------
def telegram(text, bot):

    url = "https://api.telegram.org/bot" + bot + "/sendMessage"
    print(url)
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    data = {"chat_id" : config["chat_id"], "text" : text}

    response = requests.post( url, json=data)
    print(response)

#--------
with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile)

app = Flask(__name__)

@app.route('/telegram', methods=['POST'])
def handle_push():
    if not request.json:
        abort(400)
    telegram(request.json.get('text'), config["bot"])
    return jsonify ({'status': 'ok'}) , 200

#@app.route('/json', methods=['GET', 'POST'])
#def json():
#    content = request.json
#    print (content)
#    return jsonify(content), 200

if __name__ == '__main__':
    print("Listening...")
    app.run(host=config["host"], port=5000)
