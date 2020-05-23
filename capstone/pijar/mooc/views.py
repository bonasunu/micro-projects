from django.shortcuts import render, redirect
from mooc.forms import RegisterUser 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'mooc/index.html')

@login_required(login_url='login')
def cards(request):
    return render(request, 'mooc/cards.html')

@login_required(login_url='login')
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
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        
        context = {'form': form}

        return render(request, 'mooc/register.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('cards')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('cards')
            else:
                messages.info(request, 'username OR password is incorrect')
                return render(request, 'mooc/login.html')

        return render(request, 'mooc/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def account_info(request):
    return render(request, 'mooc/account.html')