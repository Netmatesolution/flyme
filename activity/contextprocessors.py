from django.db.models.aggregates import Count
from .models import Cart
from django.db.models import Count

def cart_context(request):
    if  request.user.is_authenticated:
        cartvalue = Cart.objects.all().filter(customer=request.user,ordered=False).aggregate(Count('id'))['id__count']
    else:
        cartvalue=0
    return {
        "cartvalue":cartvalue,
    }
