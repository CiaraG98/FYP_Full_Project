from flask import Flask, redirect, url_for, render_template, jsonify, request
from interact import get_personality, reply, initialise

app = Flask(__name__)
history =[]
personality = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start_bot", methods=['GET'])
def start_bot():
    rep = initialise()
    message = {'status': "Bot Successfully Started", "message": rep}
    return jsonify(message)


@app.route("/get_persona", methods=['GET'])
def get_persona():
    global history
    global personality
    history = []
    persona, personality, key = get_personality()
    message = {'status': 'success', 'persona': persona, 'key': key}
    return jsonify(message)

@app.route("/reply_to_bot", methods=['POST', 'GET'])
def reply_to_bot():
    global history
    input = request.get_json()
    bot_reply, history = reply(input["user_reply"], history, personality)
    return jsonify({'reply': bot_reply})
        


if __name__ == "__main__":
    app.run()