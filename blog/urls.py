from django.urls import path
from .views import blogpage,Blogdetailpage

urlpatterns = [
    path('',blogpage, name="blogpage"),
    path('<slug:slug>/',Blogdetailpage.as_view(), name="productdetail"),
]