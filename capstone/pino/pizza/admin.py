from django.contrib import admin
from .models import Pasta, Salads, Platters, Pizza, Toppings, Menu

# Register your models here.
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Platters)
admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Menu)