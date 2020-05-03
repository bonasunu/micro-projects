import os

from flask import Flask, url_for, render_template
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

chList = []
chSelection = ""

@app.route("/")
def index():
    return render_template('flack.html', chList=chList)

@socketio.on("connect")
def show_last_channel():
    emit('last channel', chList)

@socketio.on("user connected")
def connected(data):
    activeUser = data["user"]
    emit('greeting', activeUser)

@socketio.on('channel creation')
def channel_creation(channel):

    if channel in chList:
        emit('channel list', 'Channel exists')
    else:
        chList.append(channel)
        emit('channel list', chList, broadcast=True)

# Join channel
@socketio.on('join channel')
def on_join(ch):
    chSelection = ch
    emit('active channel', chSelection)

# TODO
# Send message
@socketio.on('message')
def handle_message(message):
    send(message)

if __name__ == '__main__':
    socketio.run(app)
