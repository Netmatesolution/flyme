from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from core.models import Country
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(null=True,blank=True,max_length=250,unique=True)
    def __str__(self):
        return  f"{self.category}"

class Tour(models.Model):
    options =[("Excluded", "Excluded"),("Included", "Included")]
    host_id = models.ForeignKey(to=User, on_delete=models.SET_NULL,blank=True , null=True)
    verified = models.BooleanField(default=False)
    tour_name = models.CharField(max_length = 100 , unique=True)
    category = models.ForeignKey(to=Category,to_field='slug', on_delete=models.SET_NULL,blank=True , null=True)
    slug = models.SlugField(null=True,blank=True,max_length=250)
    recommended = models.BooleanField(default=False)
    highlights= models.TextField(null=True , blank=True)
    price_includes= models.TextField(null=True , blank=True)
    price_not_includes= models.TextField(null=True , blank=True)
    departure= models.CharField(max_length = 100 , blank=True)
    end= models.CharField(max_length = 100 , blank=True)
    countries= models.ForeignKey(to=Country, on_delete=models.SET_NULL,blank=True , null=True)
    cities= models.CharField(max_length = 1000 , blank=True)
    flight= models.CharField(max_length = 100 , choices = options , default='Excluded')
    guide= models.CharField(max_length = 100,choices = options,default='Excluded')
    image = models.ImageField(upload_to = "tourimg", null=True , blank=True)

    def __str__(self):
        return  f"{self.tour_name}"

class Days(models.Model):
    tour = models.ForeignKey(to=Tour, on_delete=CASCADE)
    title = models.CharField(max_length = 300)
    highlights= models.TextField(null=True , blank=True)
    visited_places = models.CharField(max_length = 1000)
    slug = models.SlugField(null=True,blank=True,max_length=250)

    def __str__(self):
        return  f"{self.title}"

class FeatureImages(models.Model):
    tour = models.ForeignKey(to=Tour, on_delete=CASCADE)
    image = models.ImageField(upload_to = "tourimg", null=True , blank=True)

    def __str__(self):
        return  f"{self.tour}"


class TourRequest(models.Model):
    tour = models.ForeignKey(to=Tour, on_delete=CASCADE)
    host_id = models.ForeignKey(to=User, on_delete=CASCADE,blank=True , null=True)
    participants=models.IntegerField(default=0)
    tour_dates=models.CharField(max_length=500,null=True, blank=True)
    accomodation = models.CharField(max_length = 100)
    budget= models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    user_name = models.CharField(max_length = 100, null=True, blank=True)
    user_email = models.CharField(max_length = 100, null=True, blank=True)
    user_number = models.CharField(max_length = 100, null=True, blank=True)
    arrival_airport=models.CharField(max_length = 100, null=True, blank=True)
    departure_airport=models.CharField(max_length = 100, null=True, blank=True)
    extension= models.TextField(null=True , blank=True)
    special_request= models.TextField(null=True , blank=True)

    def __str__(self):
        return  f"{self.user_name}"