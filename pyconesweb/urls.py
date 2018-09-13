from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('newsletter/', include('newsletter.urls')),
    path('404/', page_not_found,  {'exception': Exception()}),
    path('', include('web.urls')),
]
