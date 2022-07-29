from distutils.command.upload import upload
from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'static/images')
    Small = models.BooleanField(default=False)
    Medium = models.BooleanField(default=False)
    Large = models.BooleanField(default=False)
    description = models.TextField(max_length=120)

    def __str__(self):
        return self.name
