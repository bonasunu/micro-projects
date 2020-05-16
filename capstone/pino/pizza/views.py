from django.shortcuts import render, redirect
from django.http import HttpResponse
from pizza.forms import RegisterUser
from .models import Pizza, Toppings, Salads, Platters, Pasta, Menu
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "pizza/index.html")

def menu(request):
    context = {
        "pizza": Pizza.objects.all(),
        "toppings": Toppings.objects.all(),
        "salads": Salads.objects.all(),
        "platters": Platters.objects.all(),
        "pasta": Pasta.objects.all(),
        "menu": Menu.objects.all(),
    }
    return render(request, "pizza/menu.html", context)

@login_required(login_url='login')
def order(request):

    if request.method == 'POST':
        order = request.POST.items()
        return redirect('cart')
        # You need
        # menu_id
        # price
        # quantity

    context = {
        "pizza": Pizza.objects.all(),
        "toppings": Toppings.objects.all(),
        "salads": Salads.objects.all(),
        "platters": Platters.objects.all(),
        "pasta": Pasta.objects.all(),
        "menu": Menu.objects.all(),
    }
    return render(request, "pizza/order.html", context)

def find_us(request):
    return render(request, "pizza/find-us.html")

def register_user(request):
    if request.user.is_authenticated:
        return redirect('menu')
    else:
    
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
    if request.user.is_authenticated:
        return redirect('menu')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('menu')
            else:
                messages.info(request, 'Username OR password is incorrect')
                return render(request, 'pizza/login.html')

        return render(request, 'pizza/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def account_info(request):
    if request.user.is_authenticated:
        return render(request, 'pizza/account.html')
    else:
        return redirect('login')

def shopping_cart(request):
    if request.user.is_authenticated:
        return render(request, 'pizza/cart.html')
    else:
        return redirect('login')   