import logging

from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from twilio.twiml.messaging_response import MessagingResponse

from apps.seller.serializers.twilio import TwilioWebhookSerializer
from apps.seller.services.seller_bot import SellerBotService

logger = logging.getLogger(__name__)


class TwilioWebhook(CreateAPIView):
    serializer_class = TwilioWebhookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = MessagingResponse()
        data = serializer.validated_data
        msg = SellerBotService.get_response(data['Body'], data['From'])
        response.message(msg)
        return HttpResponse(str(response))
