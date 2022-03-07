from django.urls import path
from .views import blogpage
urlpatterns = [
    path('',blogpage, name="blogpage"),
]