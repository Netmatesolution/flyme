from django.shortcuts import render

# Create your views here.

# homepage
def homepage(request):
    ctx={}
    ctx['title'] = 'HOME'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'  
    return render(request, 'index.html',ctx)

def aboutpage(request):
    ctx={}
    ctx['title'] = 'About'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'  
    return render(request, 'about.html',ctx)