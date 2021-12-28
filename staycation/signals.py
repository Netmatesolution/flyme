from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save
from . models import *
from .utils import unique_slug_generator_staycation,unique_slug_generator_staycationroom 

@receiver(pre_save, sender=Staycation)
def save_staycation(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_staycation(instance)    


@receiver(pre_save, sender=StaycationRoom)
def save_staycation(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_staycationroom(instance)    
