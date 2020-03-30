class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):
        
        # Keep track of id number
        self.id = Flight.counter
        Flight.counter ++ 1

        