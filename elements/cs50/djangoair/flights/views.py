from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight

# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all()
    }

    return render(request, "flights/index.html", context)

def flight(request):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")

    context = {
        "flight": flight,
    }

    return render(request, "flights/flight.html", context)