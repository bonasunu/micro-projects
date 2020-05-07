from django.db import models

# Create your models here.
class RegPizza(models.Model):
    # Pizza size
    PIZZA_SIZES = (
        ('S', 'Small'),
        ('L', 'Large')
    )
    topping = models.CharField(max_length=64)
    size = models.CharField(max_length=1, choices=PIZZA_SIZES)
    price = models.FloatField()