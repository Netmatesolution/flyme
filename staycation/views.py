from django.shortcuts import render
from .models import Staycation, StaycationRoom,RoomPrice,StaycationRequest,FeatureImages
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator , PageNotAnInteger,EmptyPage
# Create your views here.

def hotelresortpage(request):
    ctx={}
    ctx['title'] = 'Hotels & Resorts'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'
    hotelsresort=Staycation.objects.all().filter(verified=True).order_by('-id')
    p = Paginator(hotelsresort,20)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    ctx['hotelsresort']=page_obj
    pagelist=[]
    for num in range(1,p.num_pages+1):
        pagelist.append(num)
    ctx['pages']=pagelist
    return render(request, 'staycation/hotels-resort.html',ctx)

def homesvillaspage(request):
    ctx={}
    ctx['title'] = 'Home & Villas'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'
    homesvillas=Staycation.objects.all().filter(verified=True,category='Home-Villas').order_by('-id')
    p = Paginator(homesvillas,20)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    ctx['homesvillas']=page_obj
    pagelist=[]
    for num in range(1,p.num_pages+1):
        pagelist.append(num)
    ctx['pages']=pagelist
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
        context['featureimages']=FeatureImages.objects.all().filter(staycation=st.id)
        return context

def staycationrequest(request):
    ctx = {}
    if request.method =='GET':  
        staycation=request.GET.get('staycation',False)
        msg=Staycation.objects.get(id=staycation)
        ctx['staycationname']=msg
        ctx['staycationid']=staycation
        ctx['rooms']=StaycationRoom.objects.all().filter(staycation=msg)
    else:
        staycationid=request.POST.get('staycationid',False)
        fullname=request.POST.get('fullname',False)
        email=request.POST.get('email',False)
        phonenumber=request.POST.get('phonenumber',False)
        # departure=request.POST.get('departure',False)
        # end=request.POST.get('end',False)
        tourdates=request.POST.get('tourdates',False)
        nights=request.POST.get('nights',False)
        roomid=request.POST.get('room',False)
        adult=request.POST.get('adult',False)
        child=request.POST.get('child',False)
        specialrequest=request.POST.get('specialrequest',False)

        staycation=Staycation.objects.get(id=staycationid)
        room=StaycationRoom.objects.get(id=roomid)
        b = StaycationRequest(host_id=staycation.host_id,staycation=staycation,full_name=fullname,
         user_email=email,user_number=phonenumber,numberofnights=nights,room=room,adult=adult,child=child,occassion=specialrequest)
        b.save()
        ctx['msg']='Your message has been sent.'
    return render(request, 'staycation/staycationrequest.html',ctx)


def staycationtheme(request):
    ctx={}
    if request.method =='GET':
        country=request.GET.get('country',False)
        theme=request.GET.get('theme',False)
        ctx['country']=country
        if theme:
            ctx['theme']=theme
            staycations=Staycation.objects.all().filter(country__slug=country,category=theme)
        else:
            staycations=Staycation.objects.all().filter(country__slug=country)

        staycationlist=staycations
        p = Paginator(staycationlist,20)
        page_number = request.GET.get('page')    
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        ctx['staycations']=page_obj
        pagelist=[]
        for num in range(1,p.num_pages+1):
            pagelist.append(num)
        ctx['pages']=pagelist
    return render(request, 'staycation/staycationtheme.html',ctx)