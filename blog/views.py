from django.shortcuts import render

# Create your views here.
def blogpage(request):
    ctx={}
    ctx['title'] = 'Blog'
    # ctx['description'] = 'HOME_PAGE_DESCRIPTION'
    # ctx['Indonesia']=Tour.objects.all().filter(countries=1,verified=True)
    return render(request, 'blog/blog.html',ctx)