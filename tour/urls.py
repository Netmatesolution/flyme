from django.urls import path
from .views import tourpage,TourDetailpage,tourrequest
urlpatterns = [
    path('',tourpage, name="tour"),
    path('request/',tourrequest, name="tourrequest"),
    path('<slug:slug>/',TourDetailpage.as_view(), name="productdetail"),   
]