from django.urls import path
from .views import hotelresortpage,homesvillaspage,StaycationDetailpage , staycationrequest
urlpatterns = [
    path('',hotelresortpage, name="hotelresort"),
    path('homes-villas',homesvillaspage, name="homesvillas"),
    path('request/',staycationrequest, name="tourrequest"),
    path('<slug:slug>/',StaycationDetailpage.as_view(), name="StaycationDetail"),      
]