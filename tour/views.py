from django.shortcuts import render
from .models import Tour,Days
from django.views.generic.detail import DetailView
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
        return context
    # def get_object(self, queryset=None):
    #     return Days.objects.get(tour=self.kwargs.get("slug"))