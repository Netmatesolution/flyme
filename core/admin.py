from django.contrib import admin
from .models import Country
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display=['name','slug']

admin.site.register(Country,CountryAdmin)
