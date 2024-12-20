# from django.contrib import admin
from django.urls import path, include

import transactions.urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("trx/", include(transactions.urls))
]
