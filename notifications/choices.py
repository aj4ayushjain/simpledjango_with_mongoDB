from django.db import models

from notifications.mediums import email, mobile_push, sms, telegram


class NotificationMediumChoices(models.IntegerChoices):
    """ choices of mediums for sending a notification """
    SMS = 1, "sms"
    EMAIL = 2, "email"
    PUSH_NOTICE = 3, "push notification"
    TELEGRAM_BOT = 4, "telegram's bot"


NOTIFICATION_MEDIUMS = {
    NotificationMediumChoices.SMS.value: sms.send_notification,
    NotificationMediumChoices.EMAIL.value: email.send_notification,
    NotificationMediumChoices.PUSH_NOTICE.value: mobile_push.send_notification,
    NotificationMediumChoices.TELEGRAM_BOT.value: telegram.send_notification,
}


