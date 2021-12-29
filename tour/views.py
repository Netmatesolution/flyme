from django.shortcuts import render
from .models import Tour,Days,TourRequest
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
# Create your views here.

# homepage
def tourpage(request):
    ctx={}
    ctx['title'] = 'Tour'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'
    ctx['Indonesia']=Tour.objects.all().filter(countries=1)
    ctx['Seychelles']=Tour.objects.all().filter(countries=2)
    ctx['SouthKorea']=Tour.objects.all().filter(countries=3)
    ctx['Japan']=Tour.objects.all().filter(countries=4)
    ctx['China']=Tour.objects.all().filter(countries=5)
    ctx['Taiwan']=Tour.objects.all().filter(countries=6)
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
    else:
        members=request.POST.get('members',False)
        tourid=request.POST.get('tourid',False)
        departure=request.POST.get('departure',False)
        end=request.POST.get('end',False)
        accomodation=request.POST.get('accomodation',False)
        fullname=request.POST.get('fullname',False)
        email=request.POST.get('email',False)
        phonenumber=request.POST.get('phonenumber',False)
        arrivalairport=request.POST.get('arrivalairport',False)
        departureairport=request.POST.get('departureairport',False)
        specialrequest=request.POST.get('specialrequest',False)

        tour=Tour.objects.get(id=tourid)
        b = TourRequest(host_id=tour.host_id,tour=tour,daparture_date=departure,end_date=end,participants=members,accomodation=accomodation,user_name=fullname,
         user_email=email,user_number=phonenumber,arrival_airport=arrivalairport,departure_airport=departureairport,special_request=specialrequest)
        b.save()
        ctx['msg']='Your message has been sent.'
    return render(request, 'tour/tourrequest.html',ctx)