from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.
class BlogModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    readonly_fields=('slug','date')

admin.site.register(Blog,BlogModelAdmin)

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('categoryquery',)

admin.site.register(Category,CategoryAdmin)