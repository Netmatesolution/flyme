from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100,unique=True)
    # slug = models.SlugField(null=True,blank=True,max_length=250,unique=True)
    def __str__(self):
        return  f"{self.name}"


