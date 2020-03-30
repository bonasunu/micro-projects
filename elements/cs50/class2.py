class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):
        
        # Keep track of id number
        self.id = Flight.counter
        Flight.counter += 1

        # Keep track of passenger
        self.passengers = []

        # Details about flight
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id


# Trying above code
# Create flight
f1 = Flight('New York', 'Paris', 540)

# Create passenger
alice = Passenger('Alice')
bob = Passenger('Bob')

# Add passenger
f1.add_passenger(alice)
f1.add_passenger(bob)

f1.print_info()