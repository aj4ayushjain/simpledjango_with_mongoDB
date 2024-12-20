from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from transactions.serializers import RequestSummarySerializer, RequestCachedSummarySerializer
from transactions.models import Transaction, TransactionSummary


class TransactionNonCachedAggregationView(APIView):
    """
    return aggregation of transactions.
    results will be generated on command and for large amount of data can take a long time.
    """
    serializer = RequestSummarySerializer

    def post(self, request):
        """
        Return a list containing aggregated values of transactions with given params(filter)
        """
        serializer = self.serializer(data=request.date)
        serializer.is_valid(raise_exception=True)
        agg_data = Transaction.get_persian_aggregated(sum_type=serializer.validated_data.get('type'),
                                                      mode=serializer.validated_data.get('mode'),
                                                      merchant_id=serializer.validated_data.get('merchantId', None))
        result = [{"key": key, "value": val} for key, val in agg_data.items()]
        return Response(data=result, status=status.HTTP_200_OK)


class TransactionCachedAggregationView(APIView):
    """
    return aggregation of transactions.
    results will be generated on command and for large amount of data can take a long time.
    """
    serializer = RequestCachedSummarySerializer

    def post(self, request):
        """
        Return a list containing aggregated values of transactions with given params(filter)
        """
        serializer = self.serializer(data=request.date)
        serializer.is_valid(raise_exception=True)
        agg_data = TransactionSummary.get_persian_aggregated(sum_type=serializer.validated_data.get('type'),
                                                             mode=serializer.validated_data.get('mode'))
        result = [{"key": key, "value": val} for key, val in agg_data.items()]
        return Response(data=result, status=status.HTTP_200_OK)
