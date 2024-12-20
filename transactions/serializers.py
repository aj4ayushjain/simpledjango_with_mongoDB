from rest_framework import serializers

from transactions.choices import TypeChoices, TimePeriodsModeChoices


class RequestSummarySerializer(serializers.Serializer):
    """ a serializer for request summary views """
    type = serializers.ChoiceField(choices=TypeChoices)
    mode = serializers.ChoiceField(choices=TimePeriodsModeChoices)
    merchantId = serializers.CharField(max_length=24, min_length=24, required=False)
