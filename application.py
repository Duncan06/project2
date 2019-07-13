import os

from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


chat = {"userschat": ""}
@app.route("/")
def index():
    return render_template("login.html")

@socket.io("message")
def chatroom:
    message = data["message"]
    chat["userchat"] = request.form.get("message")
    emit("chat", chat, broadcast=True)
