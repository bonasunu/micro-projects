from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mooc/index.html')

def cards(request):
    return render(request, 'mooc/cards.html')

def learn(request):
    return render(request, 'mooc/learn.html')

def register_user(request):
    return render(request, 'mooc/register.html')

def user_login(request):
    return render(request, 'mooc/login.html')

def account_info(request):
    return render(request, 'mooc/account.html')