from django.contrib import admin
from django.db import models
from .models import Staycation,StaycationRoom,RoomPrice , StaycationRequest,FeatureImages
from django_summernote.admin import SummernoteModelAdmin
from django import forms
from django.db import IntegrityError
from django.db import transaction
from django.contrib import messages
# Register your models here.


class StaycationChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return obj

class FeatureImagesAdmin(admin.ModelAdmin):
    list_display=('staycation',"image")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            if db_field.name == 'staycation':
                return StaycationChoiceField(queryset=Staycation.objects.all().filter(host_id=request.user))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class PageFileInline(admin.TabularInline):
        model = FeatureImages
        

class StaycationAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display = ('id','host_id','staycation_name','country')
    summernote_fields = ('highlights',)
    search_fields=['staycation_name','country__name']
    inlines = [PageFileInline,]

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
        staycation_list=super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            staycation_list=Staycation.objects.filter(host_id=request.user)
        return staycation_list

admin.site.register(Staycation,StaycationAdmin)

class StaycationChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return obj

class StaycationRoomAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display=('room_name','staycation','host_id',)
    search_fields=['room_name','staycation__staycation_name']

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            self.readonly_fields=('host_id','slug',)
        if request.user.is_superuser:
            self.readonly_fields=''
        return super().get_form(request, obj, **kwargs)

    def save_model( self, request, obj, form, change ):
        if request.user.is_staff and not request.user.is_superuser:
            obj.host_id=request.user
        obj.save()

    def get_queryset(self, request):
        rooms_list=super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            rooms_list=StaycationRoom.objects.filter(host_id=request.user)
        return rooms_list

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            if db_field.name == 'staycation':
                return StaycationChoiceField(queryset=Staycation.objects.all().filter(host_id=request.user))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(StaycationRoom,StaycationRoomAdmin)

class RoomsChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return obj

class RoomPriceAdmin(admin.ModelAdmin):
    list_display=('room_name','staycation','number_of_nights','price')
    search_fields = ['room_name__room_name','staycation__staycation_name']

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
             self.readonly_fields=('host_id',)
        if request.user.is_superuser:
            self.readonly_fields=''
        return super().get_form(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            if db_field.name == 'staycation':
                return StaycationChoiceField(queryset=Staycation.objects.all().filter(host_id=request.user))
            if db_field.name == 'room_name':
                return RoomsChoiceField(queryset=StaycationRoom.objects.all().filter(host_id=request.user))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model( self, request, obj, form, change ):
        if request.user.is_staff and not request.user.is_superuser:
            obj.host_id=request.user
        try:
            with transaction.atomic():
                obj.save()    
        except IntegrityError as e:
            messages.error(request, "This item is already added")
    
    def get_queryset(self, request):
        roomsprice_list=super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            roomsprice_list=RoomPrice.objects.filter(host_id=request.user)
        return roomsprice_list


admin.site.register(RoomPrice,RoomPriceAdmin)


admin.site.register(StaycationRequest)

# admin.site.register(FeatureImages , FeatureImagesAdmin)