import os

from flask import Flask, url_for, render_template
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

chList = []
chListMsg = {}
chSelection = ""

@app.route("/")
def index():
    return render_template('index.html', chList=chList)

@socketio.on("connect")
def show_last_channel():
    emit('last channel', chList)

@socketio.on("user connected")
def connected(data):
    activeUser = data["user"]
    emit('greeting', activeUser)

@socketio.on('channel creation')
def channel_creation(channel):

    chListMsg[channel] = []

    if channel in chList:
        emit('channel list', 'Channel exists')
    else:
        chList.append(channel)
        emit('channel list', chList, broadcast=True)

# TODO
# Implement join and leave room, send msg to room
# Join channel
@socketio.on('join channel')
def on_join(ch):
    
    chSelection = ch
    if ch in chListMsg:
        data = {"ch": ch, "msg": chListMsg[ch]}
    else:
        return False
    
    emit('active channel', data)

@socketio.on('join')
def on_join(data):
    username = data['user']
    room = data['ch']
    join_room(room)
    send(username + ' has entered the room.', room=room)

# Send message
@socketio.on('message')
def handle_message(data):
    activeChannel = data["activeChannel"]
    msg = data["msg"]
    
    chListMsg[activeChannel].append(msg)
    send(msg, broadcast=True)

    # check total messages in channel
    total = len(chListMsg[activeChannel])
    msgCh = chListMsg[activeChannel]

    if total > 100:
        del msgCh[0]

if __name__ == '__main__':
    socketio.run(app)
