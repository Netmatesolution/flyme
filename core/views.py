from django.shortcuts import render
from activity.models import Activity
from tour.models import Tour
from .models import Country,Customtrip
from staycation.models import Staycation
from blog.models import Blog
from django.db.models import Q
from django.http import JsonResponse
from .serializers import *
# Create your views here.

# homepage
def homepage(request):
    ctx={}
    ctx['title'] = 'HOME'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'  
    ctx['activites']=Activity.objects.all().filter(recommended=True,verified=True)[:4]
    ctx['tours']=Tour.objects.all().filter(recommended=True,verified=True)[:4]
    ctx['staycations']=Staycation.objects.all().filter(recommended=True,verified=True)[:4]
    ctx['blogs']=Blog.objects.all().filter(recommended=True)[:8]
    return render(request, 'index.html',ctx)

def aboutpage(request):
    ctx={}
    ctx['title'] = 'About'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'  
    return render(request, 'about.html',ctx)


def goguidepage(request):
    ctx={}
    ctx['title'] = 'Go Guide'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'  
    return render(request,'core/goguide.html',ctx)


def destination(request):
    ctx={}
    ctx['title'] = 'Destination'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'  
    return render(request, 'destination/destination.html',ctx)


def destinationdetail(request,slug):
    ctx={}
    ctx['country']=Country.objects.get(slug=slug)
    ctx['tours']=Tour.objects.all().filter(verified=True,countries=ctx['country'])
    ctx['activites']=Activity.objects.all().filter(verified=True,country=ctx['country'])
    ctx['staycations']=Staycation.objects.all().filter(verified=True,country=ctx['country'])
    return render(request, 'destination/destinationdetail.html',ctx)


def searchresults(request):
    ctx={}
    query = request.GET.get("query",None)
    activity=Activity.objects.all()
    tour=Tour.objects.all()
    staycation = Staycation.objects.all()
    ctx['activites'] = activity.filter( Q(activity_name__icontains=query) | Q(cities__icontains=query) | Q(country__name__icontains=query) | Q(category__category__icontains=query) )
    ctx['tours'] = tour.filter( Q(tour_name__icontains=query)| Q(countries__name__icontains=query) | Q(cities__icontains=query) | Q(category__category__icontains=query))
    ctx['staycations'] = staycation.filter(Q(staycation_name__icontains=query) | Q(country__name__icontains=query) | Q(category__icontains=query))
    print(ctx)
    return render(request,'core/search.html',ctx)


def customtrip(request):
    ctx={}
    if request.method =='POST':
        country=request.POST.get('country',False)
        budget=request.POST.get('budget',False)
        tourdates=request.POST.get('tourdates',False)
        fullname=request.POST.get('fullname',False)
        email=request.POST.get('email',False)
        phonenumber=request.POST.get('phonenumber',False)
        arrivalairport=request.POST.get('arrivalairport',False)
        departureairport=request.POST.get('departureairport',False)
        whom=request.POST.get('whom',False)
        adult=request.POST.get('adult',False)
        child=request.POST.get('child',False)
        specialrequest=request.POST.get('specialrequest',False)
        obj = Customtrip(country=country,budget=budget,tour_dates=tourdates,fullname=fullname,email=email,phonenumber=phonenumber,arrivalairport=arrivalairport,departureairport=departureairport,whom=whom,adult=adult,child=child,specialrequest=specialrequest)
        obj.save()
        ctx['msg']='Your message has been sent.'
    return render(request,'customtrip.html',ctx)


# view for Api
def globalSearch(request):
    type = request.GET.get("type",None)
    activity=Activity.objects.all().filter(verified=True)
    tour=Tour.objects.all().filter(verified=True)
    staycation = Staycation.objects.all().filter(verified=True)

    if type =='hotels':
        return JsonResponse(
            StaycationListSerializer(staycation,many=True).data
        ,safe=False)
    elif type == 'activity':
        return JsonResponse(ActivityListSerializer(activity,many=True).data
        ,safe=False)
    elif type == "tours":
        return JsonResponse(
            TourListSerializer(tour,many=True).data
        ,safe=False)

    if type is None:
    #     return JsonResponse([
    #         {"hotels":StaycationListSerializer(staycation,many=True).data},
    #         {"activites":ActivityListSerializer(activity,many=True).data},
    #         {"tours":TourListSerializer(tour,many=True).data},
    #     ],safe=False)
        data=StaycationListSerializer(staycation,many=True).data + ActivityListSerializer(activity,many=True).data + TourListSerializer(tour,many=True).data
        return JsonResponse(data,safe=False)



    

