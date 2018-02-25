from django.urls import path

from web.views import IndexView

urlpatterns = [
    path('', IndexView.as_view())
]
