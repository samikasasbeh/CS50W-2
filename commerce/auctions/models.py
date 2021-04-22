from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from PIL import Image


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
    image = models.ImageField( blank = True, null = True, upload_to="images/")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 :
            output_size = (126.03,100)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f"{self.title} : starting ${self.starting_bid}"


