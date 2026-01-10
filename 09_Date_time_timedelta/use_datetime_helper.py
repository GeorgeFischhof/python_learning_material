
import datetime_helper

now = datetime_helper.get_now(dt_format=datetime_helper.DateTimeFormat.NORMAL)
print("datetime_obj:", now["datetime_obj"], "type:", type(now["datetime_obj"]))
print("datetime_str:", now["datetime_str"], "type:", type(now["datetime_str"]))
