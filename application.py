import os

from flask import Flask, session, render_template, url_for, request
from flask_session import Session
from flask_socketio import SocketIO, emit

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
        return render_template("chat.html")
    if request.method == "POST":
        session['username'] = request.form.get("username")
        return render_template("chat.html")
    return render_template("index.html")

@socketio.on("message")
def chatroom(data):
    message = data["message"]
    chat["userchat"] = message
    emit("chat", chat, broadcast=True)
