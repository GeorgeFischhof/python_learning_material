
from datetime import datetime

from pytz import timezone


new_york_timezone = timezone("America/New_York")
budapest_timezone = timezone("Europe/Budapest")

new_york_time_normal = new_york_timezone.localize(datetime(2019, 3, 9, 1, 0, 0))   # before DST is set
new_york_time_dst    = new_york_timezone.localize(datetime(2019, 3, 11, 1, 0, 0))  # after DST is set

budapest_new_york_normal = new_york_time_normal.astimezone(budapest_timezone)
budapest_new_york_dst = new_york_time_dst.astimezone(budapest_timezone)

print(budapest_new_york_normal.strftime("%Y-%m-%d_%H-%M-%S"))
print(budapest_new_york_dst.strftime("%Y-%m-%d_%H-%M-%S"))


def print_all_time_zone_names_in_pytz():

    import pytz
    for time_zone in pytz.all_timezones:
        print(time_zone)
