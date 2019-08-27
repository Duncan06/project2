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
    if "username" in session:
        if "chatid" in session:
            if len(channels) >= session["chatid"]:
                return redirect(url_for('chat'))
        return redirect(url_for('chatrooms'))
    return render_template("index.html")

@app.route("/chatroom", methods=["GET", "POST"])
def chatrooms():
    if request.method == "POST":
        username = request.form.get("username")
        if username in usernames:
            return render_template("error.html", message="Username already taken.")
        usernames.append(username)
        session["username"] = username

    if request.method == "GET":
        return render_template("error.html", message="Please login.")

    return render_template("chatrooms.html", channels = channels, username=session["username"])

@app.route("/chat/<int:chatid>", methods=["GET", "POST"])
def chat(chatid):
    if request.method == "POST":
        channel_name = request.form.get("channel_name")
        if channel_name in channels:
            render_template("error.html", message="Error, channel name already exists.")

        channels.append(channel_name)
        chatdict[channel_name] = []

    if request.method == "GET":
        if username not in session:
            render_template("error.html", message="Please sign in.")
        if len(channels) < chatid:
            render_template("error.html", message="Invalid channel.")

    session["chatid"] = chatid

    render_template("chat.html", username=session["username"])

@socketio.on("message")
def chatroom(data):
    message = data["message"]
    chat = {"user": username, "messages": message}
    emit("chat", chat, broadcast=True)
