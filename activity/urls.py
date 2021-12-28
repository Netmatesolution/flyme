from django.urls import path
from .views import activitypage,ActivityDetailpage,packagedescription,addtocart,cartpage,booknow
urlpatterns = [
    path('',activitypage, name="activitypage"),
    path('cart/',cartpage, name="cartpage"),
    path('packagedescription/',packagedescription, name="packagedescription"),
    path('addtocart/',addtocart, name="addtocart"),
    path('book-now/',booknow, name="book-now"),
    path('<slug:slug>/',ActivityDetailpage.as_view(), name="ActivityDetail"),      
]