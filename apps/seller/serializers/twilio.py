from rest_framework import serializers


class TwilioWebhookSerializer(serializers.Serializer):
    MessageSid = serializers.CharField(required=False)
    SmsSid = serializers.CharField(required=False)
    AccountSid = serializers.CharField(required=True)
    From = serializers.CharField(required=True)
    To = serializers.CharField(required=True)
    Body = serializers.CharField(required=False)
