from django.test import TestCase
from flights.models import Airport, Flight

# Create your tests here.
def set_up(self):

    a1 = Airport.objects.create(code="AAA", city="City A")
    a2 = Airport.objects.create(code="BBB", city="City B")

    # Create flight
    Flight.objects.create(origin=a1, destination=a2, duration=100)
    Flight.objects.create(origin=a1, destination=a1, duration=200)
    Flight.objects.create(origin=a1, destination=a2, duration=-100)

def test_departures_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.departures.count(), 3)
