from django.db import models

# Create your models here.

class Pasta(models.Model):
    # Model
    menu = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.menu} - {self.price}"
