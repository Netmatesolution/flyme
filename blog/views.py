from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Blog

# Create your views here.
def blogpage(request):
    ctx={}
    ctx['title'] = 'Blog'
    # ctx['description'] = 'HOME_PAGE_DESCRIPTION'
    ctx['latest_article']=Blog.objects.all()
    return render(request, 'blog/blog.html',ctx)


class Blogdetailpage(DetailView):
    model=Blog
    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(Blogdetailpage,self).get_context_data(*args, **kwargs)
        # add extra field 
        # tour=Tour.objects.get(slug=self.kwargs.get("slug"))
        # context["days"] = Days.objects.all().filter(tour=tour.id) 
        # context["daycount"] = Days.objects.all().filter(tour=tour.id).count() 
        # context['featureimages']=FeatureImages.objects.all().filter(tour=tour.id)
        return context