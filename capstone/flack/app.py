import os

from flask import Flask, url_for, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

myList = []

@app.route("/")
def index():
    return render_template('index.html', myList=myList)

@socketio.on("user connected")
def connected(data):
    ch = data["connected"]
    myList.append(ch)
    emit('myList', myList, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
