from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to = "country", null=True , blank=True)
    description= models.TextField(null=True , blank=True)
    slug = models.SlugField(null=True,blank=True,max_length=250,unique=True)
    def __str__(self):
        return  f"{self.name}"


class Customtrip(models.Model):
    country=models.CharField(max_length=100,null=True,blank=True)
    budget=models.CharField(max_length=100,null=True,blank=True)
    tour_dates=models.CharField(max_length=500,null=True, blank=True)
    fullname=models.CharField(max_length=500,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phonenumber=models.CharField(max_length=100,null=True,blank=True)
    arrivalairport=models.CharField(max_length=100,null=True,blank=True)
    departureairport=models.CharField(max_length=100,null=True,blank=True)
    whom=models.CharField(max_length=100,null=True,blank=True)
    adult=models.IntegerField()
    child=models.IntegerField()
    specialrequest=models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.email}"