from django.urls import path

from newsletter.views import SubscriberCreateAPIView

urlpatterns = [
    path('subscribers/', SubscriberCreateAPIView.as_view())
]
