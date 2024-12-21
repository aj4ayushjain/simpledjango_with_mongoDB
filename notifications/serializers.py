from rest_framework import serializers

from notifications.choices import NotificationMediumChoices


class SendNotificationSerializer(serializers.Serializer):
    """ a serializer for send notification view """
    medium = serializers.ChoiceField(choices=NotificationMediumChoices)
    message = serializers.CharField()
    merchantId = serializers.CharField(max_length=24, min_length=24)


