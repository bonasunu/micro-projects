from django.shortcuts import render, redirect
from mooc.forms import RegisterUser 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'mooc/index.html')

def cards(request):
    return render(request, 'mooc/cards.html')

def learn(request):
    return render(request, 'mooc/learn.html')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('cards')
    else:

        form = RegisterUser()

        if request.method == "POST":
            form = RegisterUser(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        
        context = {'form': form}

        return render(request, 'mooc/register.html', context)

def user_login(request):
    return render(request, 'mooc/login.html')

def account_info(request):
    return render(request, 'mooc/account.html')