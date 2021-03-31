from flask import Flask, redirect, url_for, render_template, jsonify, request
from interact import get_personality, reply, initialise

app = Flask(__name__)
tokenizer = None
model = None
args = None
history = None
personality = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start_bot", methods=['GET'])
def start_bot():
    global tokenizer
    global model
    global args
    global history
    tokenizer, model, args, history = initialise()
    if tokenizer != None:
        message = {'status': "Bot Successfully Started"}
        return jsonify(message)
    else:
        return jsonify({"status": "Problem Starting Bot"})

@app.route("/get_persona", methods=['GET'])
def get_persona():
    global personality
    persona, personality, key = get_personality(tokenizer, args)
    message = {'persona': persona, 'key': key}
    return jsonify(message)

@app.route("/reply_to_bot", methods=['POST', 'GET'])
def reply_to_bot():
    input = request.get_json()
    if personality != None:
        bot_reply = reply(input["user_reply"], tokenizer, history, personality, model, args)
        return jsonify({'reply': bot_reply})


if __name__ == "__main__":
    app.run()