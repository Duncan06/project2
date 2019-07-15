import os

from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = []
usernames = []
chat = {}
@app.route("/")
def index():
    if 'username' in session:
        username = session["username"]
        return render_template("chat.html")
    if request.method == "POST":
        session['username'] = request.form.get("username")
        return render_template("chat.html")
    return render_template("index.html")

@socketio.on("message")
def chatroom():
    message = data["message"]
    chat["userchat"] = request.form.get("message")
    emit("chat", chat, broadcast=True)
