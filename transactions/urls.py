from django.urls import path

from transactions.views import TransactionNonCachedAggregationView, TransactionCachedAggregationView

urlpatterns = [
    path('non_cached_transaction_aggregation/', TransactionNonCachedAggregationView.as_view()),
    path('cached_transaction_aggregation/', TransactionCachedAggregationView.as_view()),
]
