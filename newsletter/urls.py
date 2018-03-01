from django.urls import path

from newsletter.views import SubscribersAPIView

urlpatterns = [
    path('subscribers/', SubscribersAPIView.as_view())
]
