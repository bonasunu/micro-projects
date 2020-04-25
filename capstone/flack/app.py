import os

from flask import Flask, render_template, url_for, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Channels list using python list datatype
channels = []

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("add channel")
def addChannel(data):
    channelName = data["channelName"]
    channels.append(channelName)
    
if __name__ == '__main__':
    socketio.run(app)