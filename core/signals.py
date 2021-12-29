from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save
from . models import Country
from .utils import unique_slug_generator_country

@receiver(pre_save, sender=Country)
def save_tour(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_country(instance)

