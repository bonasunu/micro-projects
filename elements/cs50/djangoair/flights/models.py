from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def is_valid_flight(self):
      return (self.origin != self.destination) and (self.duration >= 0)

    def __str__(self):
      return f"{self.id} - {self.origin} to {self.destination}"

    def clean(self):
        if self.origin == self.destination:
          raise ValidationError("Origin and destination must be different.")
        elif self.duration < 1:
          raise ValidationError("Duration must be positive.")
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)