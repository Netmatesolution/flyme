from django.shortcuts import render
from .models import Tour,Days,TourRequest , FeatureImages
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from staycation.models import Staycation
from django.core.paginator import Paginator , PageNotAnInteger,EmptyPage
# Create your views here.

# homepage
def tourpage(request):
    ctx={}
    ctx['title'] = 'Tour'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'
    ctx['tours']=Tour.objects.all().filter(verified=True)[:20]
    # ctx['Seychelles']=Tour.objects.all().filter(countries=2,verified=True)
    # ctx['SouthKorea']=Tour.objects.all().filter(countries=3,verified=True)
    # ctx['Japan']=Tour.objects.all().filter(countries=4,verified=True)
    # ctx['China']=Tour.objects.all().filter(countries=5,verified=True)
    # ctx['Taiwan']=Tour.objects.all().filter(countries=6,verified=True)
    # ctx['staycations']=Staycation.objects.all().filter(recommended=True,verified=True)[:4]
    return render(request, 'tour/tour.html',ctx)


# product detail page
class TourDetailpage(DetailView):
    model=Tour
    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(TourDetailpage,self).get_context_data(*args, **kwargs)
        # add extra field 
        tour=Tour.objects.get(slug=self.kwargs.get("slug"))
        context["days"] = Days.objects.all().filter(tour=tour.id) 
        context["daycount"] = Days.objects.all().filter(tour=tour.id).count() 
        context['featureimages']=FeatureImages.objects.all().filter(tour=tour.id)
        return context
    # def get_object(self, queryset=None):
    #     return Days.objects.get(tour=self.kwargs.get("slug"))


def tourrequest(request):
    ctx = {}
    if request.method =='GET':  
        tour=request.GET.get('tour',False)
        msg=Tour.objects.get(id=tour)
        ctx['tourname']=msg
        ctx['tourid']=tour
    elif request.method == 'POST':
        members=request.POST.get('members',False)
        tourid=request.POST.get('tourid',False)
        tourdates=request.POST.get('tourdates',False)
        accomodation=request.POST.get('accomodation',False)
        fullname=request.POST.get('fullname',False)
        email=request.POST.get('email',False)
        phonenumber=request.POST.get('phonenumber',False)
        arrivalairport=request.POST.get('arrivalairport',False)
        departureairport=request.POST.get('departureairport',False)
        specialrequest=request.POST.get('specialrequest',False)
        tour=Tour.objects.get(id=tourid)
        b = TourRequest(host_id=tour.host_id,tour=tour,tour_dates=tourdates,participants=members,accomodation=accomodation,user_name=fullname,
         user_email=email,user_number=phonenumber,arrival_airport=arrivalairport,departure_airport=departureairport,special_request=specialrequest)
        b.save()
        ctx['msg']='Your message has been sent.'
    return render(request, 'tour/tourrequest.html',ctx)


def tourtheme(request):
    ctx={}
    if request.method =='GET':
        country=request.GET.get('country',False)
        theme=request.GET.get('theme',False)
        ctx['country']=country

        if theme:
            ctx['theme']=theme
            tours=Tour.objects.all().filter(countries__slug=country,category__slug=theme)
        else:
            tours=Tour.objects.all().filter(countries__slug=country)

        tourlist = tours
        
        p = Paginator(tourlist,20)
        page_number = request.GET.get('page')    
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        ctx['tours']=page_obj
        pagelist=[]
        for num in range(1,p.num_pages+1):
            pagelist.append(num)
        ctx['pages']=pagelist

    return render(request, 'tour/tourtheme.html',ctx)