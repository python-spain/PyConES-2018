from django.urls import path

from web.views import IndexView, DetailsView, TalkDetail

urlpatterns = [
    path(r'talk/<slug:slug>', TalkDetail.as_view(), name="talk_details"),
    path(r'<path:path>', DetailsView.as_view(), name="details"),
    path('', IndexView.as_view()),
]
