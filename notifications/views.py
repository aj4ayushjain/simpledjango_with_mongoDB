from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from notifications.serializers import SendNotificationSerializer
from notifications.tasks import send_notification


class SendNotificationView(APIView):
    """
    used to send notification using different mediums
    """
    serializer = SendNotificationSerializer

    def post(self, request):
        """
        Return satus 200 if no exception arise
        """
        serializer = self.serializer(data=request.date)
        serializer.is_valid(raise_exception=True)
        send_notification.apply_async(medium=serializer.validated_data.get("medium"),
                                      merchant_id=serializer.validated_data.get("merchantId"),
                                      message=serializer.validated_data.get("message"))
        return Response(status=status.HTTP_200_OK)

