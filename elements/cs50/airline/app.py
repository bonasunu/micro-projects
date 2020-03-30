from flask import Flask, request, render_template
import os
from models import *

app = Flask(__name__)
app.comfig['SQL_ALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/')
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number")

    # Make sure the flight exists
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight with that id")

    # Add passenger
    passenger = Passenger(name=name, flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()
    return render_template("sucess.html")

@app.route('/flights')
def flights():
    """List all flights"""
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route('/flights/<int:flight_id>')
def flight(flight_id):
    # Make sure flight exist
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight")

    # Get all passengers
    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    return render_template("flight.html", flight=flight, passengers=passengers)