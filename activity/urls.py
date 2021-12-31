from django.urls import path
from .views import activitypage,ActivityDetailpage,packagedescription,addtocart,cartpage,booknow,staycationtheme
urlpatterns = [
    path('',activitypage, name="activitypage"),
    path('cart/',cartpage, name="cartpage"),
    path('packagedescription/',packagedescription, name="packagedescription"),
    path('addtocart/',addtocart, name="addtocart"),
    path('book-now/',booknow, name="book-now"),
    path('theme/', staycationtheme, name='staycationtheme'),
    path('<slug:slug>/',ActivityDetailpage.as_view(), name="ActivityDetail"),      
]