import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABSE_URL"))

db = scoped_session(sessionmaker(bind=engine))

flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
for flight in flights:
    print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes."
    
