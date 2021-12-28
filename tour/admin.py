from django.contrib import admin
from django.db.models import fields
from django.http import request
from django import forms
from .models import Category,Tour,Days,FeatureImages
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class TourAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display = ('id','host_id','tour_name','verified')
    summernote_fields = ('highlights','price_includes','price_not_includes')

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
        tour_list=super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            tour_list=Tour.objects.filter(host_id=request.user)
        return tour_list

class CategoryAdmin(admin.ModelAdmin):
    list_display=('category','slug')
    readonly_fields=('slug',)


class TourChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return obj

class DaysAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    summernote_fields=('highlights')
    list_display = ('title','tour',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            if db_field.name == 'tour':
                return TourChoiceField(queryset=Tour.objects.all().filter(host_id=request.user))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class FeatureImagesAdmin(admin.ModelAdmin):
    list_display=('tour',"image")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            if db_field.name == 'tour':
                return TourChoiceField(queryset=Tour.objects.all().filter(host_id=request.user))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(FeatureImages , FeatureImagesAdmin)
admin.site.register(Tour,TourAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Days,DaysAdmin)
