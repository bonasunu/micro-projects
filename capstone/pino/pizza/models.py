from django.db import models

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