from collections import defaultdict
import mongoengine


class Transaction(mongoengine.Document):
    """ containing information about a single transaction related to a user """
    merchantId = mongoengine.ObjectIdField(required=True)
    amount = mongoengine.IntField(min_value=1)
    createdAt = mongoengine.DateTimeField(required=True)

    @classmethod
    def aggregate_daily_amount_sum(cls) -> list[dict[str, int]]:
        """
        will return sum of all transaction amount, aggregated daily
        it will not return dates with 0 amount
        """
        iran_time_difference = (3 * 60 * 60 + 30 * 60) * 1000
        pipelines = [
            {
                '$addFields': {
                    'iranLocalTime': {
                        '$add': [
                            '$createdAt',  # UTC datetime field
                            iran_time_difference  # timedelta in milliseconds
                        ]
                    }
                }
            },
            {
                '$group': {
                    '_id': {
                        '$dateToString': {
                            'format': '%Y-%m-%d',
                            'date': '$iranLocalTime'
                        }
                    },
                    'totalAmount': {
                        '$sum': '$amount'  # Sum the amount field
                    }
                }
            },
            {
                '$sort': {
                    '_id': 1  # Sort by date
                }
            }
        ]

        return cls.objects.aggregate(*pipelines)

    @classmethod
    def aggregate_daily_count_sum(cls) -> list[dict[str, int]]:
        """
        will return sum of all transaction count, aggregated daily
        it will not return dates with 0 transaction
        """
        iran_time_difference = (3 * 60 * 60 + 30 * 60) * 1000
        pipelines = [
            {
                '$addFields': {
                    'iranLocalTime': {
                        '$add': [
                            '$createdAt',  # UTC datetime field
                            iran_time_difference  # timedelta in milliseconds
                        ]
                    }
                }
            },
            {
                '$group': {
                    '_id': {
                        '$dateToString': {
                            'format': '%Y-%m-%d',
                            'date': '$iranLocalTime'
                        }
                    },
                    'totalAmount': {
                        '$sum': 1  # for each record add one
                    }
                }
            },
            {
                '$sort': {
                    '_id': 1  # Sort by date
                }
            }
        ]

        return cls.objects.aggregate(*pipelines)

