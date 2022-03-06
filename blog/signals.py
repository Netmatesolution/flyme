from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save
from . models import Blog , Category
from blog.utils import unique_slug_generator_blog , unique_category_query

@receiver(pre_save, sender=Blog)
def save_blog(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_blog(instance)    


@receiver(pre_save, sender=Category)
def save_category(sender, instance, *args, **kwarg):
    if not instance.categoryquery:
        instance.categoryquery = unique_category_query(instance) 