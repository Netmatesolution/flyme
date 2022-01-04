from django.shortcuts import render
from .models import Activity,Package, Packageprice,Cart,Order,Category,FeatureImages
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Min,Max,Sum,F , Q
from staycation.models import Staycation
# Create your views here.

def activitypage(request):
    ctx={}
    ctx['title'] = 'Activity'
    ctx['description'] = 'HOME_PAGE_DESCRIPTION'
    ctx['Indonesia']=Activity.objects.all().filter(country=1,verified=True)
    ctx['Seychelles']=Activity.objects.all().filter(country=2,verified=True)
    ctx['SouthKorea']=Activity.objects.all().filter(country=3,verified=True)
    ctx['Japan']=Activity.objects.all().filter(country=4,verified=True)
    ctx['China']=Activity.objects.all().filter(country=5,verified=True)
    ctx['Taiwan']=Activity.objects.all().filter(country=6,verified=True)
    ctx['staycations']=Staycation.objects.all().filter(recommended=True,verified=True)[:4]
    return render(request, 'activity/activity.html',ctx)



class ActivityDetailpage(DetailView):
    model=Activity

    def get_context_data(self, *args, **kwargs):
        context = super(ActivityDetailpage,self).get_context_data(*args, **kwargs)
        activity=Activity.objects.get(slug=self.kwargs.get("slug"))
        packagelist=Package.objects.all().filter(activity_name=activity).values('package_name','slug','id',)
        context['packages']=packagelist
        context['featureimages']=FeatureImages.objects.all().filter(activity=activity.id)
        return context


def packagedescription(request):
    ctx={}
    packageid=request.GET.get('packageid',False)
    packagedesc=Package.objects.get(id=packageid)
    packageprice=Packageprice.objects.all().filter(package=packageid).values()
    ctx['description']=packagedesc.description
    ctx['packageprice']=list(packageprice)
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


def staycationtheme(request):
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
        ctx['activites']=activites
    return render(request, 'activity/activitytheme.html',ctx)