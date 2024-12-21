import mongoengine

from notifications.choices import NotificationMediumChoices


class Notifications(mongoengine.Document):
    """ containing information each notification sent to a user """
    createdAt = mongoengine.DateTimeField(required=True)
    merchantId = mongoengine.ObjectIdField(required=True)
    medium = mongoengine.IntField(choices=NotificationMediumChoices.choices, required=True)
    destination = mongoengine.StringField(required=True)
    message = mongoengine.StringField(required=True)



