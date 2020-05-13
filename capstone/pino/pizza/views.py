from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.
def index(request):
    return render(request, "pizza/index.html")

def menu(request):
    context = {
        "pizza": Pizza.objects.all()
    }
    return render(request, "pizza/menu.html", context)

def order(request):
    return render(request, "pizza/order.html")

def find_us(request):
    return render(request, "pizza/find-us.html")