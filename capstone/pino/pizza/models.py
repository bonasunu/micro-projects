from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pasta(models.Model):
    # Model
    menu = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.menu} - {self.price}"

class Salads(models.Model):
    salad = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.salad} - {self.price}"

class Platters(models.Model):
    SALAD_SIZE = (
        ("S", "Small"),
        ("L", "Large")
    )

    platter = models.CharField(max_length=64)
    size = models.CharField(max_length=1, choices=SALAD_SIZE)
    price = models.FloatField()

    def __str__(self):
        return f"{self.platter} - {self.size} - {self.price}"

class Pizza(models.Model):
    PIZZA_SIZE = (
        ("S", "Small"),
        ("L", "Large")
    )

    PIZZA_TYPE = (
        ("Reguler", "Reguler"),
        ("Sicilian","Sicilian")
    )

    pizza_type = models.CharField(max_length=8, choices=PIZZA_TYPE)
    pizza_menu = models.CharField(max_length=64)
    size = models.CharField(max_length=1, choices=PIZZA_SIZE)
    price = models.FloatField()

class Toppings(models.Model):
    PIZZA_TOPPINGS = (
        ("Pepperoni", "Pepperoni"),
        ("Sausage", "Sausage"),
        ("Mushrooms", "Mushrooms"),
        ("Onions", "Onions"),
        ("Ham", "Ham"),
        ("Canadian Bacon", "Canadian Bacon"),
        ("Pineapple", "Pineapple"),
        ("Eggplant", "Eggplant"),
        ("Tomato & Basil", "Tomato & Basil"),
        ("Green Peppers", "Green Peppers"),
        ("Hamburger","Hamburger"),
        ("Spinach","Spinach"),
        ("Artichoke", "Artichoke"),
        ("Buffalo Chicken", "Buffalo Chicken"),
        ("Barbecue Chicken","Barbecue Chicken"),
        ("Anchovies", "Anchovies"),
        ("Black Olives", "Black Olives"),
        ("Fresh Gralic", "Fresh Gralic"),
        ("Zucchini", "Zucchini")
    )

    topping = models.CharField(max_length=64, choices=PIZZA_TOPPINGS)

class Menu(models.Model):
    MENU_CATEGORY = (
        ("pizza", "pizza"),
        ("pasta", 'pasta'),
        ("subs", "subs"),
        ("platters", 'platters'),
        ("toppings", "toppings"),
        ("salads", "salads")
    )

    MENU_SIZE = (
        ("Small", "Small"),
        ("Large", "Large")
    )

    MENU_PIZZA_TYPE = (
        ("Reguler", "Reguler"),
        ("Sicilian","Sicilian")
    )
    
    menu_id = models.AutoField(primary_key=True)
    menu_category = models.CharField(max_length=10, choices=MENU_CATEGORY)
    menu_name = models.CharField(max_length=64)
    menu_pizza_type = models.CharField(max_length=8, choices=MENU_PIZZA_TYPE, blank=True)
    size = models.CharField(max_length=6, choices=MENU_SIZE, blank=True)
    price = models.FloatField()

class Order(models.Model):
    PAYMENT_STATUS = (
        ("Paid", "Paid"),
        ("Pending", "Pending")
    )

    ORDER_STATUS = (
        ("Pending", "Pending"),
        ("On Process", "On Process"),
        ("Complete","Complete")
    )

    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usernames")
    order = models.CharField(max_length=10000)
    payment_status = models.CharField(max_length=8, choices=PAYMENT_STATUS)
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS)