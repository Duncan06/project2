import os

from flask import Flask, session, render_template, url_for, request, jsonify, redirect
from flask_session import Session
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__, template_folder='../../scripts/project2')
app.config['SESSION_TYPE'] = 'filesystem'
app.config["SECRET_KEY"] = 'k45wenk12nlsdfi8547jnk335j3'
socketio = SocketIO(app)
Session(app)

channels = []
usernames = []
chat = {}
@app.route("/", methods=["GET", "POST"])
def index():
    if 'username' in session:
        username = session["username"]
        return redirect(url_for('chat'))
    if request.method == "POST":
        username = request.form.get("username")
        if username in usernames:
            return render_template("error.html", message="Username already taken.")
        usernames.append(username)
        session['username'] = username
        return redirect(url_for('chat'))
    return render_template("index.html")

@app.route("/chatroom", methods=["GET", "POST"])
def chatrooms():
    if request.method == "POST":

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        return jsonify(chat)

@socketio.on("message")
def chatroom(data):
    message = data["message"]
    chat = {"user": username, "messages": message}
    emit("chat", chat, broadcast=True)
