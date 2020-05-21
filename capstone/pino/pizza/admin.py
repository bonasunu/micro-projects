from django.contrib import admin
from .models import Pasta, Salads, Platters, Pizza, Toppings, Menu, Order

# Register your models here.
admin.site.register(Menu)
admin.site.register(Order)