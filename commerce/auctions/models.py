from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.category}'

class List(models.Model):
    title = models.CharField(max_length=64)
    created_date = models.DateTimeField(default= timezone.now)
    description = models.TextField()
    starting_bid= models.FloatField()
    current_bid = models.FloatField(blank= True, null=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name="Category")
    creator = models.ForeignKey(User, on_delete= models.PROTECT, related_name="Creator_lists")

    def __str__(self):
        return f"{self.title} : starting ${self.starting_bid}"

    
