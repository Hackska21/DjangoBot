from rest_framework import serializers


class MsgSerializer(serializers.Serializer):
    msg = serializers.CharField(max_length=255)
    user_id = serializers.CharField(max_length=255)
