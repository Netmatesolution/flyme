from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', admin.site.urls),
    path('',include('core.urls')),
    path('tour/',include('tour.urls')),
    path('blog/',include('blog.urls')),
    path('staycation/',include('staycation.urls')),
    path('activity/',include('activity.urls')),
    path('accounts/',include('registration.backends.default.urls')),
    path('summernote/',include('django_summernote.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
