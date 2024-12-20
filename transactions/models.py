import mongoengine
from pymongo import UpdateOne
from bson import ObjectId

from transactions.choices import TypeChoices, TimePeriodsModeChoices
from transactions.utils import (fill_missing_dates_with_zero, convert_date_to_jajli_numberic_day,
                                aggregate_date_key_to_jalali_week, aggregate_date_key_to_jalali_monthly)


class Transaction(mongoengine.Document):
    """ containing information about a single transaction related to a user """
    merchantId = mongoengine.ObjectIdField(required=True)
    amount = mongoengine.IntField(min_value=1)
    createdAt = mongoengine.DateTimeField(required=True)

    @classmethod
    def aggregate_daily_amount_sum(cls, user_id: str | None = None) -> list[dict[str, int]]:
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
                    'total': {
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
        if user_id is not None:
            pipelines.insert(0, cls.user_id_filter_pipeline(user_id))

        return list(cls.objects.aggregate(*pipelines))

    @classmethod
    def aggregate_daily_count_sum(cls, user_id: str | None = None) -> list[dict[str, int]]:
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
                    'total': {
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
        if user_id is not None:
            pipelines.insert(0, cls.user_id_filter_pipeline(user_id))

        return list(cls.objects.aggregate(*pipelines))

    @staticmethod
    def user_id_filter_pipeline(user_id: str):
        """ will return match pipeline for a given id """
        return {'$match': {'merchantId': ObjectId(user_id)}}

    @classmethod
    def get_persian_aggregated(cls, sum_type: str, mode: str, merchant_id: str | None = None):
        """
        will return transactions aggregated data according to given params in persian and jalali date
        :param sum_type in ["amount", "count"]
        :param mode in ["daily", "weekly", "monthly"]
        :param merchant_id: type: str
        """
        if sum_type not in TypeChoices or mode not in TimePeriodsModeChoices:
            raise ValueError(f"param sum_type:{sum_type}, or param mode:{mode} is not an acceptable choice.")

        if sum_type == TypeChoices.AMOUNT:
            aggregated = fill_missing_dates_with_zero(cls.aggregate_daily_amount_sum(user_id=merchant_id))
        elif sum_type == TypeChoices.COUNT:
            aggregated = fill_missing_dates_with_zero(cls.aggregate_daily_count_sum(user_id=merchant_id))

        if mode == TimePeriodsModeChoices.DAILY:
            return convert_date_to_jajli_numberic_day(aggregated=aggregated)
        elif mode == TimePeriodsModeChoices.WEEKLY:
            return aggregate_date_key_to_jalali_week(aggregated=aggregated)
        elif mode == TimePeriodsModeChoices.MONTHLY:
            return aggregate_date_key_to_jalali_monthly(aggregated=aggregated)


class TransactionSummary(mongoengine.Document):
    """ containing contain aggregated values and count of transactions per day """
    amount = mongoengine.IntField(min_value=0)
    count = mongoengine.IntField(min_value=0)
    date = mongoengine.DateTimeField(unique=True)

    @staticmethod
    def update_transaction_summary():
        """ will create or update transaction aggregated data in TransactionSummary collection """
        operations = []
        daily_amount: dict = fill_missing_dates_with_zero(Transaction.aggregate_daily_amount_sum())
        daily_count: dict = fill_missing_dates_with_zero(Transaction.aggregate_daily_count_sum())

        for day in daily_amount:
            operations.append(UpdateOne({'date': day},
                                        {'$set': {'amount': daily_amount[day], 'count': daily_count[day]}},
                                        upsert=True))
        if operations:
            db = mongoengine.connection.get_db()
            db.transaction_summary.bulk_write(operations)

    @classmethod
    def get_persian_aggregated(cls, sum_type: str, mode: str):
        """
        will return transactions aggregated data according to given params in persian and jalali date
        :param sum_type in ["amount", "count"]
        :param mode in ["daily", "weekly", "monthly"]
        """
        if sum_type not in TypeChoices or mode not in TimePeriodsModeChoices:
            raise ValueError(f"param sum_type:{sum_type}, or param mode:{mode} is not an acceptable choice.")

        if sum_type == TypeChoices.AMOUNT:
            aggregated = {item.date: item.amount for item in cls.objects.only('amount', 'date').order_by('date')}
        elif sum_type == TypeChoices.COUNT:
            aggregated = {item.date: item.count for item in cls.objects.only('count', 'date').order_by('date')}

        if mode == TimePeriodsModeChoices.DAILY:
            return convert_date_to_jajli_numberic_day(aggregated=aggregated)
        elif mode == TimePeriodsModeChoices.WEEKLY:
            return aggregate_date_key_to_jalali_week(aggregated=aggregated)
        elif mode == TimePeriodsModeChoices.MONTHLY:
            return aggregate_date_key_to_jalali_monthly(aggregated=aggregated)

