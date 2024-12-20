from django.db import models


class TypeChoices(models.TextChoices):
    """ choices related to request summary 'type' field """
    AMOUNT = "amount", "amount"
    COUNT = "count", "count"


class TimePeriodsModeChoices(models.TextChoices):
    """ choices related to request summary 'mode' field """
    daily = "daily", "daily"
    weekly = "weekly", "weekly"
    monthly = "monthly", "monthly"






