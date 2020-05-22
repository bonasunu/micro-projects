from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.user_login, name='login'),
    path('register', views.register_user, name='register'),
    path('cards', views.cards, name='cards'),
    path('learn', views.learn, name='learn'),
]