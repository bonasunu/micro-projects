from django.shortcuts import render, redirect
from django.http import HttpResponse
from pizza.forms import RegisterUser
from .models import Pizza, Toppings, Salads, Platters, Pasta, Menu, Order
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import math

# Variables on server-side
user_order = {}
"""
user_order = {
    "current_user": [
        {"menu_id": name,
        "menu_name": item.menu_name,
        "qty": qty,
        "item_price": item.price,
        "total_price": math.floor(float(request.POST.get(name))) * item.price},
    ]
}
"""

# Create your views here.
def index(request):
    return render(request, "pizza/index.html")

def menu(request):
    context = {
        "menu": Menu.objects.all(),
    }
    return render(request, "pizza/menu.html", context)

@login_required(login_url='login')
def order(request):

    if request.method == 'POST':
        order = {}
        user_order[request.user.username] = []
        items = Menu.objects.all()
        for item in items:
            name = str(item.menu_id)
            qty = math.floor(float(request.POST.get(name)))

            current_user = request.user.username
            
            user_order[current_user].append({
                "menu_id": name,
                "menu_name": item.menu_name,
                "qty": qty,
                "item_price": item.price,
                "total_price": math.floor(float(request.POST.get(name))) * item.price
            })

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
        context = {
            "username": request.user,
            "order": Order.objects.all(),
        }
        return render(request, 'pizza/account.html', context)
    else:
        return redirect('login')

def shopping_cart(request):
    if request.user.is_authenticated:

        try:
            user_order[request.user.username]
        except KeyError:
            return redirect('order')
        context = {
                "user_order": user_order[request.user.username],
        }

        if request.method == 'POST': 
            return redirect('payment')

        return render(request, 'pizza/cart.html', context)
    else:
        return redirect('login')

@login_required(login_url='login')
def payment(request):
    if request.method == 'POST':
        try:
            context = {
            "var": user_order[request.user.username],
            }

            customer_order = context["var"]
        except KeyError:
            return redirect('order')

        context = {
        "var": user_order[request.user.username],
        }

        customer_order = context["var"]

        order = Order()
        order.order = ""

        for item in customer_order:
            if item['qty'] > 0:
                order.order += " (" + item['menu_name'] + " - Qty : " + str(item['qty']) +") "

        order.customer = request.user
        order.payment_status = "Paid"
        order.order_status = "Pending"
        order.save()

        user_order[request.user.username] = []

        return redirect('account-info')

    try:
        context = {
        "var": user_order[request.user.username],
        }

        customer_order = context["var"]
    except KeyError:
        return redirect('order')

    context = {
        "var": user_order[request.user.username],
    }

    return render(request, 'pizza/payment.html', context)