import mongoengine


class Transaction(mongoengine.Document):
    """ containing information about a single transaction related to a user """
    merchantId = mongoengine.ObjectIdField(required=True)
    amount = mongoengine.IntField(min_value=1)
    createdAt = mongoengine.DateTimeField(required=True)


