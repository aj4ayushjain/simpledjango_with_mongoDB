from collections import defaultdict
import datetime


def convert_to_datetime(date: str) -> datetime.datetime:
    """ will take a string with a formate like '2023-06-29' and return it with datetime type """
    date_format = "%Y-%m-%d"
    return datetime.datetime.strptime(date, date_format)


def fill_mossing_dates_with_zero(aggregated: list) -> dict[datetime.datetime, int]:
    """
    will add missing dates to date list and add zero for value
    note: given list must be pre_ordered in ascending order by date.
    """

    if len(aggregated) < 2:
        # in case of aggregated results being less than 2
        if len(aggregated) == 0:
            return {}
        return {convert_to_datetime(aggregated[0]["id"]): aggregated[0]["total"]}

    first_date = convert_to_datetime(aggregated[0]["id"])
    last_date = convert_to_datetime(aggregated[-1]["id"])
    pivot_date = first_date

    aggregated_dict = defaultdict(int, {convert_to_datetime(item["id"]): item["total"] for item in aggregated})
    zero_filled_dict = {}
    while pivot_date < last_date:
        zero_filled_dict[pivot_date] = aggregated_dict[pivot_date]
        pivot_date = pivot_date + datetime.timedelta(days=1)

    return zero_filled_dict


def convert_date_key_to_jalali(aggregated: dict[datetime.datetime, int]) -> dict[datetime.datetime, int]:
    """ will translate given dictionaries keys and return another dict with jalali keys """
    ...


