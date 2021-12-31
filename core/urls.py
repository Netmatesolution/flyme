from django.urls import path
from .views import homepage,aboutpage,destination,destinationdetail,searchresults,customtrip
urlpatterns = [
    path('',homepage, name="home"),
    path('about/',aboutpage, name="about"),
    path('destination/',destination, name="destination"),
    path('tailormade/',customtrip, name="customtrip"),
    path('search/', searchresults, name='search_results'),
    path('destination/<slug:slug>/',destinationdetail, name="destinationdetail"),
   
]