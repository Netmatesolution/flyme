from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Category(models.Model):
    category= models.CharField(max_length = 100,unique=True)
    categoryquery = models.SlugField(null=True,blank=True,max_length=250,unique=True)
    def __str__(self):
        return  f"{self.category}"



class Blog(models.Model):
    title = models.CharField(max_length = 100)
    category=models.ForeignKey(to=Category, on_delete=CASCADE,to_field="categoryquery",blank=True , null=True)
    featured = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)
    slug = models.SlugField(null=True,blank=True,max_length=250)
    content = models.TextField()
    last_edit = models.DateField(auto_now_add=True)
    status = models.CharField(max_length = 100 , default='publish',  choices=(('publish','publish'), ('draft','draft')))
    img=models.ImageField(upload_to = "blogs", null=True)
    
    def __str__(self):
        return  f"{self.title}"
