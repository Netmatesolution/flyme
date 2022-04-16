from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from core.models import Country
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(null=True,blank=True,max_length=250)
    def __str__(self):
        return  f"{self.category}"

class Activity(models.Model):
    host_id = models.ForeignKey(to=User, on_delete=CASCADE,blank=True , null=True)
    verified = models.BooleanField(default=False,)
    slug = models.SlugField(null=True,blank=True,max_length=250)
    recommended = models.BooleanField(default=False)
    activity_name = models.CharField(max_length = 100 , unique=True)
    country= models.ForeignKey(to=Country, on_delete=models.SET_NULL,blank=True , null=True)
    cities= models.CharField(max_length = 1000 , blank=True)
    category = models.ForeignKey(to=Category,to_field='category', on_delete=CASCADE,blank=True , null=True)
    highlights= models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to = "featureimg", null=True , blank=True)
    video_id =  models.CharField( max_length=5000 , default='None')
    overview = models.TextField(null=True,blank=True)
    what_to_expect = models.TextField(null=True,blank=True)
    latitude=models.CharField(max_length = 100 , unique=True,null=True,blank=True)
    longitude=models.CharField(max_length = 100 , unique=True,null=True,blank=True)

    def __str__(self):
        return  f"{self.activity_name}"



class Package(models.Model):
    host_id = models.ForeignKey(to=User, on_delete=CASCADE,blank=True , null=True)
    activity_name = models.ForeignKey(to=Activity, on_delete=CASCADE,blank=True , null=True)
    slug = models.SlugField(null=True,blank=True,max_length=250)
    package_name = models.CharField(max_length = 100)
    activity_duration = models.CharField(max_length=200,null=True,blank=True) 
    description= models.TextField(null=True,blank=True)
    inclusions= models.TextField(null=True,blank=True)
    requirements= models.TextField(null=True,blank=True)
    mon =  models.BooleanField(default=False)
    tue =  models.BooleanField(default=False)
    wed =  models.BooleanField(default=False)
    thu =  models.BooleanField(default=False)
    fri =  models.BooleanField(default=False)
    sat =  models.BooleanField(default=False)
    sun =  models.BooleanField(default=False)

    def __str__(self):
        return  f"{self.package_name}"



class Packageprice(models.Model):
    host_id = models.ForeignKey(to=User, on_delete=CASCADE,blank=True , null=True)
    activity_name = models.ForeignKey(to=Activity, on_delete=CASCADE,blank=True , null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    minimumCount= models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)


    class Meta:
        unique_together = ('activity_name', 'package','name','host_id')

    def __str__(self):
        return  f"{self.name}"



class Order(models.Model):
    customer = models.ForeignKey(to=User,on_delete=CASCADE,null=True, blank=True)
    firstname=models.CharField(max_length=500,default='')
    lastname=models.CharField(max_length=500,default='')
    email=models.CharField(max_length=500,default='')
    mobile=models.CharField(max_length=12,default='')
    address=models.CharField(max_length=1000,default='')
    country=models.CharField(max_length=50,default='')
    state=models.CharField(max_length=50,default='')
    zipcode=models.CharField(max_length=20,default='')
    paymenttype=models.CharField(max_length=50,default='')
    total = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.id}"

# cart_status =(
#     ("In Process", "In Process"),
#     ("Packing", "Packing"),
#     ("Out For Delivery", "Out For Delivery"),
#     ("Delivered", "Delivered"),
#     ("Cancel", "Cancel"),
#     ("Return", "Return"),
# )

class Cart(models.Model):
    order = models.ForeignKey(to=Order,on_delete=CASCADE,null=True,blank=True)
    # id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(to=User,on_delete=CASCADE,null=True, blank=True)
    product = models.ForeignKey(to=Packageprice,on_delete=CASCADE,null=True, blank=True)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    # status = models.CharField(choices = cart_status,default='In Process',max_length = 100 )

    def __str__(self):
        return  f"{self.id}"


class FeatureImages(models.Model):
    activity = models.ForeignKey(to=Activity, on_delete=CASCADE)
    image = models.ImageField(upload_to = "activityimg", null=True , blank=True)

    def __str__(self):
        return  f"{self.activity}"



class Reviews(models.Model):
    customer = models.ForeignKey(to=User,on_delete=CASCADE,null=True, blank=True)
    verified = models.BooleanField(default=False,)
    firstname=models.CharField(max_length=500,default='')
    lastname=models.CharField(max_length=500,default='')
    activity_name = models.ForeignKey(to=Activity, on_delete=CASCADE,blank=True , null=True)
    message=models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.customer}"