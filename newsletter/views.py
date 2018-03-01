import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from newsletter.forms import SubscriberForm
from newsletter.utils import SubscribeMail

logger = logging.getLogger(__name__)


class SubscribersAPIView(APIView):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        form = SubscriberForm(data=request.data)
        if form.is_valid():
            try:
                email = form.cleaned_data['email']
                SubscribeMail.create(email)
                return Response(status=status.HTTP_201_CREATED)
            except Exception as ex:
                logger.error(str(ex))
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_400_BAD_REQUEST)
