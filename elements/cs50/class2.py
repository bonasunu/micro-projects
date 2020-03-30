class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):
        
        # Keep track of id number
        self.id = Flight.counter
        Flight.counter += 1

        # Keep track of passenger
        self.passenger = []

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

    