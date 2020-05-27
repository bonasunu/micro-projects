from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.user_login, name='login'),
    path('register', views.register_user, name='register'),
    path('cards', views.cards, name='cards'),
    path('learn', views.learn, name='learn'),
    path('account', views.account_info, name='account'),
    path('logout', views.user_logout, name='logout'),
    path('add_category', views.add_category, name='add_category'),
    path('add_card', views.add_card, name='add_card'),
    path('delete_category', views.delete_category, name='delete_category'),
    path('flashcards', views.flashcards, name='flashcards'),
]