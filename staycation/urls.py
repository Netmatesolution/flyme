from django.urls import path
from .views import hotelresortpage,homesvillaspage,StaycationDetailpage , staycationrequest,staycationtheme
urlpatterns = [
    path('',hotelresortpage, name="hotelresort"),
    path('homes-villas',homesvillaspage, name="homesvillas"),
    path('request/',staycationrequest, name="staycationrequest"),
    path('theme/', staycationtheme, name='staycationtheme'),
    path('<slug:slug>/',StaycationDetailpage.as_view(), name="StaycationDetail"),      
]