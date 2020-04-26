import os

from flask import Flask, render_template, url_for, jsonify, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Channels list using python list datatype
channelList = {"Total": 0}

@app.route("/")
def index():
    return render_template("index.html", channelList=channelList)

@socketio.on("add channel")
def addchannel(data):
    channelList.append(data["chName"])
    
if __name__ == '__main__':
    socketio.run(app)