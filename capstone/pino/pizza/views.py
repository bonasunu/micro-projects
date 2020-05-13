from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "pizza/index.html")

def menu(request):
    return render(request, "pizza/menu.html")

def order(request):
    return render(request, "pizza/order.html")

def find_us(request):
    return render(request, "pizza/find-us.html")