import logging

from mailchimp3.mailchimpclient import MailChimpError
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from newsletter.serializers import SubscriberSerializer

logger = logging.getLogger(__name__)


class SubscriberCreateAPIView(CreateAPIView):
    serializer_class = SubscriberSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            except MailChimpError as ex:
                logger.error(str(ex))
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_400_BAD_REQUEST)
