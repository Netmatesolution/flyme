from multiprocessing.dummy import JoinableQueue
from django.shortcuts import render
from .models import Activity,Package, Packageprice,Cart,Order,Category,FeatureImages,Reviews
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Min,Max,Sum,F , Q
from staycation.models import Staycation
from django.core.paginator import Paginator , PageNotAnInteger,EmptyPage
# Create your views here.

def activitypage(request):
    ctx={}
    ctx['title'] = 'Activity'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'
    ctx['count']=Activity.objects.all().filter(verified=True).count()
    ctx['activites']=Activity.objects.all().filter(verified=True)[:20]
    ctx['categories']=Category.objects.all()
    # ctx['Seychelles']=Activity.objects.all().filter(country=2,verified=True)
    # ctx['SouthKorea']=Activity.objects.all().filter(country=3,verified=True)
    # ctx['Japan']=Activity.objects.all().filter(country=4,verified=True)
    # ctx['China']=Activity.objects.all().filter(country=5,verified=True)
    # ctx['Taiwan']=Activity.objects.all().filter(country=6,verified=True)
    # ctx['staycations']=Staycation.objects.all().filter(recommended=True,verified=True)[:4]
    return render(request, 'activity/activity.html',ctx)



class ActivityDetailpage(DetailView):
    model=Activity

    def get_context_data(self, *args, **kwargs):
        context = super(ActivityDetailpage,self).get_context_data(*args, **kwargs)
        activity=Activity.objects.get(slug=self.kwargs.get("slug"))
        packagelist=Package.objects.all().filter(activity_name=activity).values('package_name','slug','id',)
        context['packages']=packagelist
        context['featureimages']=FeatureImages.objects.all().filter(activity=activity.id)
        context['reviews']=Reviews.objects.all().filter(activity_name=activity.id,verified=True)
        return context


def packagedescription(request):
    ctx={}
    packageid=request.GET.get('packageid',False)
    packagedesc=Package.objects.get(id=packageid)
    packageprice=Packageprice.objects.all().filter(package=packageid).values()
    ctx['description']=packagedesc.description
    ctx['packageprice']=list(packageprice)
    return JsonResponse(ctx,safe=False)

def loadactivity(request):
    ctx={}
    category=request.POST.get('category',False)
    ctx['activites']=list(Activity.objects.all().filter(verified=True,category__slug=category).values('activity_name','slug','image','cities','category')[:20])
    ctx['count']=Activity.objects.all().filter(verified=True,category__slug=category).count()
    return JsonResponse(ctx,safe=False)

def loadmoredata(request):
    ctx={}    
    start = int(request.POST.get('row',False))
    end = start+20
    ctx['activites']=list(Activity.objects.all().filter(verified=True).values('activity_name','slug','image','cities','category')[start:end])
    return JsonResponse(ctx,safe=False)

@login_required
def addtocart(request):
    ctx = {}
    if request.method == "POST":
        data=request.POST
        for pid,qt in data.items():
            print(f'id:{pid} quantity : {qt}')            
            productobj=Packageprice.objects.get(id=pid)
            ctx[f'{productobj.name}']={}
            userid = request.user
            msg = Cart.objects.get_or_create(customer=userid,product=productobj,ordered=False)
            print(msg)
            cartid=msg[0].id
            if int(qt) != 0:
                Cart.objects.filter(id=cartid).update(quantity=qt)
            if msg[1]:
                ctx[f'{productobj.name}'][f'msg-{pid}'] = "Added to cart"
                ctx[f'{productobj.name}'][f'activityname-{pid}']=productobj.activity_name.activity_name
                ctx[f'{productobj.name}'][f'packagename-{pid}']=productobj.package.package_name
                ctx[f'{productobj.name}'][f'status-{pid}']="success"
            else:
                ctx[f'{productobj.name}'][f'msg-{pid}'] = "Already in cart,cart updated "
                ctx[f'{productobj.name}'][f'activityname-{pid}']=productobj.activity_name.activity_name
                ctx[f'{productobj.name}'][f'packagename-{pid}']=productobj.package.package_name
                ctx[f'{productobj.name}'][f"status-{pid}"]="error"
                if int(qt)==0:
                    qty=Cart.objects.get(id=cartid)
                    if qty.quantity == 0:
                        Cart.objects.filter(id=cartid).delete()
                        ctx[f'{productobj.name}'][f'msg-{pid}'] = "Deleted from cart"
                    else:
                        ctx[f'{productobj.name}'][f'msg-{pid}'] = "Already in cart,cart updated "
        return JsonResponse(ctx)


# cart page
@login_required
def cartpage(request):
    ctx={}
    ctx['title'] = 'Cart'
    ctx['cart'] = Cart.objects.all().filter(customer=request.user,ordered=False)
    carttotal= Cart.objects.all().filter(customer=request.user,ordered=False).select_related().aggregate(total=Sum(F('product__price')*F('quantity')))
    ctx['carttotal'] = carttotal['total']
    return render(request, 'activity/cart.html',ctx)


# booknow page
@login_required
def booknow(request):
    ctx={}
    # ctx['activitylist']=Cart.objects.all().filter(customer=request.user,ordered=False).values("product__activity_name__activity_name").distinct()
    ctx['title'] = 'Checkout'
    ctx['cart'] = Cart.objects.all().filter(customer=request.user,ordered=False)
    carttotal= Cart.objects.all().filter(customer=request.user,ordered=False).select_related().aggregate(total=Sum(F('product__price')*F('quantity')))
    ctx['carttotal'] = carttotal['total']
    if request.method =='GET':
        ctx['msg1'] = ""
    else:
        first_name=request.POST.get('firstname',False)    
        last_name=request.POST.get('lastname',False)    
        mail=request.POST.get('email',False)    
        mob=request.POST.get('mobile',False)    
        addr=request.POST.get('address',False)    
        nation=request.POST.get('country',False)    
        area=request.POST.get('state',False)    
        zip=request.POST.get('zipcode',False)
        payment_type=request.POST.get('paymenttype',False)
        carttotal= Cart.objects.all().filter(customer=request.user,ordered=False).select_related().aggregate(total=Sum(F('product__price')*F('quantity')))['total']        
        msg=Order.objects.get_or_create(customer=request.user,firstname=first_name,lastname=last_name,email=mail,mobile=mob,address=addr,country=nation,state=area,zipcode=zip,paymenttype=payment_type,total=carttotal)
        if msg[1]:
            ctx['msg1'] = "Order is placed"
            ctx['status']="success"
        else:
            ctx['msg1'] = "Something went wrong! Try after few minutes"
            ctx["status"]="error"    
    return render(request, 'activity/book-now.html',ctx)


def activitytheme(request):
    ctx={}
    if request.method =='GET':
        country=request.GET.get('country',False)
        theme=request.GET.get('theme',False)
        ctx['country']=country
        ctx['categories']=Category.objects.all()
        if theme:
            ctx['theme']=theme
            activites=Activity.objects.all().filter(country__slug=country,category__slug=theme)
        else:
            activites=Activity.objects.all().filter(country__slug=country)
        activitylist=activites
        p = Paginator(activitylist,20)
        page_number = request.GET.get('page')    
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
        ctx['activites']=page_obj
        pagelist=[]
        for num in range(1,p.num_pages+1):
            pagelist.append(num)
        ctx['pages']=pagelist
    return render(request, 'activity/activitytheme.html',ctx)

@login_required
def deleteitem(request):
    ctx={}
    if request.method == "POST":
        cartid=request.POST.get('cartid',False)
        msg = Cart.objects.filter(id=cartid).delete()
        if msg:
            ctx['msg']='Item deleted from cart'
    return JsonResponse(ctx)
        


def reviews(request):
    ctx={}
    if request.method =='POST':
        message=request.POST.get('message',False)
        id=int(request.POST.get('id',False))
        activity = Activity.objects.get(id=id)
        firstname=request.user.first_name
        lastname=request.user.last_name
        msg=Reviews.objects.get_or_create(customer=request.user,message=message,activity_name=activity,firstname=firstname,lastname=lastname)
        if msg[1]:
            ctx['msg1'] = "Thanks for your feedback."
            ctx['status']="success"
        else:
            ctx['msg1'] = "Something went wrong! Try after few minutes"
            ctx["status"]="error"    
    return JsonResponse(ctx)