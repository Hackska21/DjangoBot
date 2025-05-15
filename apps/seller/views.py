from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.seller.services.seller_bot import SellerBotService


class MsgSerializer(serializers.Serializer):
    msg = serializers.CharField(max_length=255)
    user_id = serializers.CharField(max_length=255)


class SimpleChatbotEndpoint(CreateAPIView):
    serializer_class = MsgSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        msg = SellerBotService.get_response(data['msg'], data['user_id'])
        return Response(msg)
