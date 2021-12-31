from django.urls import path
from .views import tourpage,TourDetailpage,tourrequest, tourtheme
urlpatterns = [
    path('',tourpage, name="tour"),
    path('request/',tourrequest, name="tourrequest"),
    path('theme/', tourtheme, name='tourtheme'),
    path('<slug:slug>/',TourDetailpage.as_view(), name="productdetail"),   
]