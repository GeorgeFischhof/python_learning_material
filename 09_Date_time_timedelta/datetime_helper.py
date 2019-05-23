
import datetime


class DateTimeFormat:
    NORMAL = '%Y-%m-%d %H:%M:%S'
    COMPACT = '%Y%m%d_%H%M%S'
    COMPACT_WITH_US = '%Y%m%d_%H%M%S_%f'


def get_now(dt_format=DateTimeFormat.COMPACT) -> dict:
    now = datetime.datetime.now()
    now_datetime_str = datetime_obj_to_datetime_str(now, dt_format)
    now_datetime_obj = datetime_str_to_datetime_obj(now_datetime_str, dt_format)

    now = {'datetime_obj': now_datetime_obj, 'datetime_str': now_datetime_str,}
    return now


def datetime_obj_to_datetime_str(datetime_obj, dt_format=DateTimeFormat.COMPACT) -> str:
    datetime_str = datetime.datetime.strftime(datetime_obj, dt_format)
    return datetime_str


def datetime_str_to_datetime_obj(datetime_str, dt_format=DateTimeFormat.COMPACT) -> datetime.datetime:
    datetime_obj = datetime.datetime.strptime(datetime_str, dt_format)
    return datetime_obj
