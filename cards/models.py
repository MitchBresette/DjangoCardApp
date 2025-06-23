from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    rarity = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def clean(self):
        super().clean()
        if self.price < 0:
            raise ValidationError({"price: 'Price cannot be below zero"})


    def __str__(self):
        return f"{self.name} ({self.type})"
