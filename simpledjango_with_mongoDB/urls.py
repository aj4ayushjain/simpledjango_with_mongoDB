from django.urls import path, include

import transactions.urls
import notifications.urls

urlpatterns = [
    path("trx/", include(transactions.urls)),
    path("notification/", include(notifications.urls))
]
