from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


import transactions.urls
import notifications.urls

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path("trx/", include(transactions.urls)),
    path("notification/", include(notifications.urls))
]
