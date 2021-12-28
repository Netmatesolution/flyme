from django.contrib import admin
from .models import Activity,Category,Package, Packageprice,Cart,Order
from django_summernote.admin import SummernoteModelAdmin
from django import forms
from django.db import IntegrityError
from django.db import transaction
from django.contrib import messages
# Register your models here.

class ActivityAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display=('id','activity_name','verified')
    summernote_fields = ('highlights','overview')

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            self.readonly_fields=('slug','host_id','verified')
            self.exclude=('recommended',)
            self.list_editable=''
        if request.user.is_superuser:
            self.readonly_fields=('slug',)
            self.exclude=''
            self.list_editable=('verified',)
        return super().get_form(request, obj, **kwargs)

    def save_model( self, request, obj, form, change ):
        if request.user.is_staff and not request.user.is_superuser:
            obj.host_id=request.user
        obj.save()

    def get_queryset(self, request):
        activity_list=super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            activity_list=Activity.objects.filter(host_id=request.user)
        return activity_list


admin.site.register(Activity,ActivityAdmin)
admin.site.register(Category)


class ActivityChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return obj

class PackageAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display=('id','package_name','activity_name')
    summernote_fields = ('description','inclusions','requirements')

    def get_queryset(self, request):
        package_list=super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            package_list=Package.objects.filter(host_id=request.user)
        return package_list

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            self.readonly_fields=('slug','host_id',)
        if request.user.is_superuser:
            self.readonly_fields=('slug',)
            self.exclude=''
        return super().get_form(request, obj, **kwargs)

    def save_model( self, request, obj, form, change ):
        if request.user.is_staff and not request.user.is_superuser:
            obj.host_id=request.user
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            if db_field.name == 'activity_name':
                return ActivityChoiceField(queryset=Activity.objects.all().filter(host_id=request.user))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Package,PackageAdmin)

class PackageChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return obj

class PackagepriceAdmin(admin.ModelAdmin):
    list_display=('id','activity_name','package','name','price',)

    def get_queryset(self, request):
        packageprice_list=super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            packageprice_list=Packageprice.objects.filter(host_id=request.user)
        return packageprice_list

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            self.readonly_fields=('host_id',)
        if request.user.is_superuser:
            self.readonly_fields=''
        return super().get_form(request, obj, **kwargs)

    def save_model( self, request, obj, form, change ):
        if request.user.is_staff and not request.user.is_superuser:
            obj.host_id=request.user
        try:
            with transaction.atomic():
                obj.save()    
        except IntegrityError as e:
            messages.error(request, "This item is already added")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            if db_field.name == 'activity_name':
                return ActivityChoiceField(queryset=Activity.objects.all().filter(host_id=request.user))
            if db_field.name == 'package':
                return PackageChoiceField(queryset=Package.objects.all().filter(host_id=request.user))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Packageprice,PackagepriceAdmin)


class CartInline(admin.TabularInline):
    model = Cart
    readonly_fields = ('customer','product','quantity','ordered')
    def get_max_num(self, request, obj=None, **kwargs):
        max_num = 0
        return max_num
    def has_delete_permission(self, request, obj=None):
        return False

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','total']
    inlines = [CartInline,]

admin.site.register(Order,OrderAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display=['id','product','quantity','ordered']
    list_editable=['ordered']
    search_fields=['id']

admin.site.register(Cart,CartAdmin)