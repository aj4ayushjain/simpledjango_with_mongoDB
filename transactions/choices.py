from django.db import models


class TypeChoices(models.TextChoices):
    """ choices related to request summary 'type' field """
    AMOUNT = "amount", "amount"
    COUNT = "count", "count"


class TimePeriodsModeChoices(models.TextChoices):
    """ choices related to request summary 'mode' field """
    DAILY = "daily", "daily"
    WEEKLY = "weekly", "weekly"
    MONTHLY = "monthly", "monthly"






