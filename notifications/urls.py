from django.urls import path

from notifications.views import SendNotificationView

urlpatterns = [
    path('send_notification/', SendNotificationView.as_view()),
]
