from django.urls import path
from .views import tourpage,TourDetailpage
urlpatterns = [
    path('',tourpage, name="tour"),
    path('<slug:slug>/',TourDetailpage.as_view(), name="productdetail"),   
]