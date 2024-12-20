from collections import defaultdict
import datetime

from persiantools import jdatetime

def convert_to_datetime(date: str) -> datetime.datetime:
    """ will take a string with a formate like '2023-06-29' and return it with datetime type """
    date_format = "%Y-%m-%d"
    return datetime.datetime.strptime(date, date_format)


def fill_missing_dates_with_zero(aggregated: list) -> dict[datetime.datetime, int]:
    """
    will add missing dates to date list and add zero for value
    note: given list must be pre_ordered in ascending order by date.
    """

    if len(aggregated) < 2:
        # in case of aggregated results being less than 2
        if len(aggregated) == 0:
            return {}
        return {convert_to_datetime(aggregated[0]["_id"]): aggregated[0]["total"]}

    first_date = convert_to_datetime(aggregated[0]["_id"])
    last_date = convert_to_datetime(aggregated[-1]["_id"])
    pivot_date = first_date

    aggregated_dict = defaultdict(int, {convert_to_datetime(item["_id"]): item["total"] for item in aggregated})
    zero_filled_dict = {}
    while pivot_date < last_date:
        zero_filled_dict[pivot_date] = aggregated_dict[pivot_date]
        pivot_date = pivot_date + datetime.timedelta(days=1)

    return zero_filled_dict


def convert_date_key_to_jalali(aggregated: dict[datetime.datetime, int]) -> dict[jdatetime, int]:
    """ will translate given dictionaries keys and return another dict with jalali keys """
    result = {}
    for key, val in aggregated.items():
        new_key = jdatetime.JalaliDateTime.to_jalali(key)
        result[new_key] = val
    return result


def convert_date_to_jajli_numberic_day(aggregated: dict[datetime.datetime, int]) -> dict[str, int]:
    """ will dict with keys of jalali type to string type, like 1402/04/02 """
    result = {}
    for key, val in aggregated.items():
        new_key = jdatetime.JalaliDateTime.to_jalali(key)
        result[new_key.strftime("%Y/%m/%d")] = val
    return result


def aggregate_date_key_to_jalali_week(aggregated: dict[datetime.datetime, int]) -> dict[str, int]:
    """ will translate given aggregated-ordered dict to jalali calender and aggregate days into weeks """
    aggregated = convert_date_key_to_jalali(aggregated=aggregated)
    result = defaultdict(int)
    for key, val in aggregated.items():
        result[key.strftime("سال %Y هفته %W")] += val
    return dict(result)


def aggregate_date_key_to_jalali_monthly(aggregated: dict[datetime.datetime, int]) -> dict[str, int]:
    """ will translate given aggregated-ordered dict to jalali calender and aggregate days into monthly """
    aggregated = convert_date_key_to_jalali(aggregated=aggregated)
    result = defaultdict(int)
    for key, val in aggregated.items():
        result[key.strftime("%Y %B", locale="fa")] += val
    return dict(result)

