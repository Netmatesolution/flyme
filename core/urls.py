from django.urls import path
from .views import homepage,aboutpage
urlpatterns = [
    path('',homepage, name="home"),
    path('about/',aboutpage, name="about"),
   
]