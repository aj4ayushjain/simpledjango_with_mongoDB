from rest_framework import serializers

from transactions.choices import TypeChoices, TimePeriodsModeChoices


class RequestSummarySerializer(serializers.Serializer):
    """ a serializer for request summary view """
    type = serializers.ChoiceField(choices=TypeChoices)
    mode = serializers.ChoiceField(choices=TimePeriodsModeChoices)
    merchantId = serializers.CharField(max_length=24, min_length=24, required=False)


class RequestCachedSummarySerializer(serializers.Serializer):
    """ a serializer for request cached summary view | it does not supper merchantId """
    type = serializers.ChoiceField(choices=TypeChoices)
    mode = serializers.ChoiceField(choices=TimePeriodsModeChoices)
