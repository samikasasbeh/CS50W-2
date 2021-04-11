from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Lists(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f'{self.title}: Starting price {self.price} '

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass

