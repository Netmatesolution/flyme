from django.shortcuts import render
from activity.models import Activity
from tour.models import Tour
from .models import Country
from staycation.models import Staycation
from django.db.models import Q
# Create your views here.

# homepage
def homepage(request):
    ctx={}
    ctx['title'] = 'HOME'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'  
    ctx['activites']=Activity.objects.all().filter(recommended=True,verified=True)[:4]
    ctx['tours']=Tour.objects.all().filter(recommended=True,verified=True)[:4]
    ctx['staycations']=Staycation.objects.all().filter(recommended=True,verified=True)[:4]
    return render(request, 'index.html',ctx)

def aboutpage(request):
    ctx={}
    ctx['title'] = 'About'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'  
    return render(request, 'about.html',ctx)

def destination(request):
    ctx={}
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



# Q(cities__icontains=query)| Q(category__icontains=query) | Q(country__icontains=query) |
# Q(countries__icontains=query)| | Q(tour_cities__icontains=query)| Q(category__icontains=query)
# | Q(country__icontains=query)| Q(category__icontains=query)