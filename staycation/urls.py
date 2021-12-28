from django.urls import path
from .views import hotelresortpage,homesvillaspage,StaycationDetailpage
urlpatterns = [
    path('',hotelresortpage, name="hotelresort"),
    path('homes-villas',homesvillaspage, name="homesvillas"),
    path('<slug:slug>/',StaycationDetailpage.as_view(), name="StaycationDetail"),      
]