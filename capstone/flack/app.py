import os

from flask import Flask, url_for, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

chList = []

@app.route("/")
def index():
    return render_template('index.html', chList=chList)

@socketio.on("connect")
def show_last_channel():
    emit('last channels', chList, broadcast=True)

@socketio.on("user connected")
def connected(data):
    activeUser = data["user"]
    emit('greeting', activeUser)

@socketio.on('channel creation')
def channel_creation(channel):
    chList.append(channel)
    emit('channel list', chList, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
