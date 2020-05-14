from django.shortcuts import render, redirect
from django.http import HttpResponse
from pizza.forms import RegisterUser
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

def register_user(request):
    
    form = RegisterUser()

    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/menu')
    
    context = {'form': form}

    return render(request, "pizza/register.html", context)

def login(request):
    return render(request, 'pizza/login.html')