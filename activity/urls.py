from django.urls import path
from .views import activitypage,ActivityDetailpage,packagedescription,addtocart,cartpage,booknow,activitytheme, deleteitem,loadactivity
urlpatterns = [
    path('',activitypage, name="activitypage"),
    path('cart/',cartpage, name="cartpage"),
    path('packagedescription/',packagedescription, name="packagedescription"),
    path('addtocart/',addtocart, name="addtocart"),
    path('deleteitem/',deleteitem, name="deleteitem"),
    path('book-now/',booknow, name="book-now"),
    path('theme/', activitytheme, name='activitytheme'),
    path('loadactivity/',loadactivity,name='loadactivity'),
    path('<slug:slug>/',ActivityDetailpage.as_view(), name="ActivityDetail"),      
]