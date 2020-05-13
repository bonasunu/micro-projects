from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is Pizza!")

def menu(request):
    return HttpResponse("This is menu")