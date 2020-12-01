from flask import Flask, redirect, url_for, render_template, jsonify, request
from interact import run, reply

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello", methods=['GET'])
def hello():
    #GET req
    message = {'greeting': 'Hello from Flask!'}
    return jsonify(message)

@app.route("/invoke_bot", methods=['GET'])
def invoke_bot():
    persona = run()
    message = {'persona': persona}
    return jsonify(message)

@app.route("/reply_to_bot", methods=['POST', 'GET'])
def reply_to_bot():
    input = request.get_json()
    bot_reply = reply(input["user_reply"])
    return jsonify({'reply': bot_reply})

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()