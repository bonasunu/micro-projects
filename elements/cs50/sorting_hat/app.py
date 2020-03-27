import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gryffindor")
def gryffindor():
    return render_template("gryffindor.html")

@app.route("/slytherin")
def slytherin():
    return render_template("slytherin.html")

@app.route("/planes", methods=['GET'])
def plane():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == '__main __':
    app.run(debug=True)