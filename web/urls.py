from django.urls import path

from web.views import IndexView, DetailsView

urlpatterns = [
    path(r'details/<path:path>', DetailsView.as_view(), name="details"),
    path('', IndexView.as_view())
]
