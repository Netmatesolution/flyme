from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save,post_save
from . models import Activity , Category , Package , Order , Cart
from activity.utils import unique_slug_generator_activity , unique_slug_generator_category,unique_slug_generator_package

@receiver(pre_save, sender=Activity)
def save_activity(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_activity(instance)    

@receiver(pre_save, sender=Category)
def save_activity(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_category(instance)  

@receiver(pre_save, sender=Package)
def save_package(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_package(instance)

@receiver(post_save, sender=Order)
def save_product(sender, instance, *args, **kwarg):
    if instance:
        orderid=instance.id
        user=instance.customer
        msg=Cart.objects.all().filter(customer=user,ordered=False).update(ordered=True,order=orderid)
        # print(msg)