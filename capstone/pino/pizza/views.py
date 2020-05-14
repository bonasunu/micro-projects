from django.shortcuts import render, redirect
from django.http import HttpResponse
from pizza.forms import RegisterUser
from .models import Pizza
from django.contrib import messages

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
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    
    context = {'form': form}

    return render(request, "pizza/register.html", context)

def user_login(request):
    return render(request, 'pizza/login.html')