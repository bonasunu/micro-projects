from django.shortcuts import render, redirect
from mooc.forms import RegisterUser 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Category, Cards


# Create your views here.
def index(request):
    return render(request, 'mooc/index.html')

@login_required(login_url='login')
def cards(request):
    categories = Category.objects.all()
    cards = Cards.objects.all()
    user = request.user

    context = {
        "categories": categories,
        "cards": cards,
        'user': user
    }

    return render(request, 'mooc/cards.html', context)

@login_required(login_url='login')
def add_category(request):
    
    if request.method == 'POST':
        category = request.POST.get('add_category')
        add_category = Category()

        add_category.category = category
        add_category.user = request.user
        add_category.save()

        return redirect('cards')

@login_required(login_url='login')
def add_card(request):

    if request.method == 'POST':
        card_category = request.POST.get('select_category')
        card_question = request.POST.get('card_question')
        card_answer = request.POST.get('card_answer')

        add_card = Cards()
        add_card.card_category = Category.objects.get(category=card_category)
        add_card.card_question = card_question
        add_card.card_answer = card_answer

        add_card.save()
        # TODO add message 
        return redirect('cards')

@login_required(login_url='login')
def learn(request):

    category = Category.objects.all()
    cards = Cards.objects.all()
    user = request.user

    context = {
        'category': category,
        'cards': cards,
        'user': user
    }

    if request.method == 'POST':
        card_category = request.POST.get('learn_category')
        cards = Cards.objects.all()
        user = request.user
        learn_card = {}

        for item in cards:
            if item.card_category.user == user and item.card_category.category == card_category:
                learn_card[item.card_question] = item.card_answer

        # add feature - show a number of cards based on user preference

        context = {
            'card_category': card_category,
            'cards': cards,
            'user': user,
            'learn_card': learn_card
        }
        
        # TODO add JSONmethod for random pick card feature
        return render(request, 'mooc/flashcards.html', context)

    return render(request, 'mooc/learn.html', context)

@login_required(login_url='login')
def flashcards(request):

    return render(request, 'mooc/flashcards.html', context)

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

@login_required(login_url='login')
def account_info(request):
    return render(request, 'mooc/account.html')