from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save
from . models import *
from .utils import unique_slug_generator_tour , unique_slug_generator_themes 
from django.contrib.auth.models import User

@receiver(pre_save, sender=Tour)
def save_tour(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_tour(instance)

@receiver(pre_save, sender=Category)
def save_category(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_themes(instance)    
