from datetime import datetime
from bson import ObjectId
from celery import shared_task

from notifications.choices import NOTIFICATION_MEDIUMS, NotificationMediumChoices
from notifications.models import Notifications
from transactions.models import Transaction

@shared_task
def send_notification(medium: int, merchant_id: str, message: str):
    """ used to send notifications with any medium """
    get_destination_for_merchant = lambda x: '0000_0000'  # dummy function that will retrieves merchant's address by its id
    destination = get_destination_for_merchant(merchant_id)
    notice = Notifications(
        createdAt=datetime.now(),
        merchantId=ObjectId(merchant_id),
        medium=medium,
        destination=destination,
        message=message
    )
    notice.save()

    NOTIFICATION_MEDIUMS[medium](destination, message)



@shared_task
def notify_today_transaction_sum():
    """ used to send sum of today's transaction for each merchant by email and sms """
    merchants = ["63a69a2d18f9347bdafd5e10"]  # fake list of all merchants retrieved from fake database
    for merchant in merchants:
        summary = Transaction.get_last_day_transaction_summary_by_merchant(merchant_id=merchant)
        send_notification.delay(medium=NotificationMediumChoices.SMS, merchant_id=merchant, message=str(summary))
        send_notification.delay(medium=NotificationMediumChoices.EMAIL, merchant_id=merchant, message=str(summary))










