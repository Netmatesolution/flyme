from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from core.models import Country
# Create your models here.

class Staycation(models.Model):
    category_list = [
        ('Hotel-Resorts','Hotel & Resorts'),
        ('Home-Villas','Home & Villas'),
    ]
    host_id = models.ForeignKey(to=User, on_delete=CASCADE,blank=True , null=True)
    staycation_name = models.CharField(max_length = 100 , unique=True)
    slug = models.SlugField(null=True,blank=True,max_length=500)
    category = models.CharField(max_length = 100 , choices = category_list , default='Hotel & Resorts')
    recommended = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    highlights= models.TextField(null=True , blank=True)
    video_id =  models.CharField( max_length=5000 , default='None')
    country= models.ForeignKey(to=Country, on_delete=models.SET_NULL,blank=True , null=True)
    feature_image = models.ImageField(upload_to = "staycation", null=True , blank=True)
    logo =models.ImageField(upload_to='staycation',null=True,blank=True)

    def __str__(self):
        return  f"{self.staycation_name}"

class StaycationRoom(models.Model):
    host_id = models.ForeignKey(to=User, on_delete=CASCADE,blank=True , null=True)
    staycation=models.ForeignKey(to=Staycation,on_delete=CASCADE,blank=True , null=True)
    room_name = models.CharField(max_length = 100,null=True,blank=True)
    description = models.TextField(null=True , blank=True)
    slug = models.SlugField(null=True,blank=True,max_length=500)
    inclusion = models.TextField(null=True , blank=True)
    roomfacilites = models.TextField(null=True , blank=True)
    roompolicies = models.TextField(null=True , blank=True)
    feature_image = models.ImageField(upload_to = "staycation", null=True , blank=True)
    
    def __str__(self):
        return  f"{self.room_name}"


class RoomPrice(models.Model):
    host_id = models.ForeignKey(to=User, on_delete=CASCADE,blank=True , null=True)
    staycation=models.ForeignKey(to=Staycation,on_delete=CASCADE,blank=True , null=True)
    room_name=models.ForeignKey(to=StaycationRoom,on_delete=CASCADE,blank=True , null=True)
    number_of_nights = models.CharField(max_length = 100 ,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)

    class Meta:
        unique_together = ('staycation', 'room_name','number_of_nights','host_id')

    def __str__(self):
        return f"{self.room_name}"



class StaycationRequest(models.Model):
    host_id = models.ForeignKey(to=User, on_delete=CASCADE,blank=True , null=True)
    staycation = models.ForeignKey(to=Staycation, on_delete=CASCADE)
    full_name = models.CharField(max_length = 100,null=True, blank=True)
    user_email = models.CharField(max_length = 100, null=True, blank=True)
    user_number = models.CharField(max_length = 100, null=True, blank=True)
    tour_dates=models.CharField(max_length=500,null=True, blank=True)
    numberofnights=models.IntegerField(null=True,blank=True)
    adult=models.IntegerField(null=True,blank=True)
    child=models.IntegerField(null=True,blank=True)
    room = models.ForeignKey(to=StaycationRoom, on_delete=CASCADE,blank=True , null=True)
    occassion=models.CharField(max_length = 100, null=True, blank=True)

    def __str__(self):
        return  f"{self.user_email}"

class FeatureImages(models.Model):
    staycation = models.ForeignKey(to=Staycation, on_delete=CASCADE)
    image = models.ImageField(upload_to = "staycationimg", null=True , blank=True)

    def __str__(self):
        return  f"{self.staycation}"

