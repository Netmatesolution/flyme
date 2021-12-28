from django.shortcuts import render
from .models import Staycation, StaycationRoom,RoomPrice
from django.views.generic.detail import DetailView
# Create your views here.

def hotelresortpage(request):
    ctx={}
    ctx['title'] = 'Hotels & Resorts'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'
    ctx['hotelsresort']=Staycation.objects.all().filter(verified=True,category='Hotel & Resorts').order_by('-id')
    return render(request, 'staycation/hotels-resort.html',ctx)

def homesvillaspage(request):
    ctx={}
    ctx['title'] = 'Home & Villas'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'
    ctx['homesvillas']=Staycation.objects.all().filter(verified=True,category='Home & Villas').order_by('-id')
    return render(request, 'staycation/homes-villas.html',ctx)


# product detail page
class StaycationDetailpage(DetailView):
    model=Staycation
    def get_context_data(self, *args, **kwargs):
        context = super(StaycationDetailpage,self).get_context_data(*args, **kwargs)
        st=Staycation.objects.get(slug=self.kwargs.get("slug"))
        datadict={}
        roomlist=StaycationRoom.objects.all().filter(staycation=st)
        for room in roomlist: 
            datadict[room.room_name]={}
            roomprice=RoomPrice.objects.all().filter(room_name=room)
            datadict[room.room_name]['room']=room
            datadict[room.room_name]['price']=roomprice
        context['data']=datadict
        return context