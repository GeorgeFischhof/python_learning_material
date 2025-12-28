# datetime.timedelta

<https://docs.python.org/3/library/datetime.html#datetime.timedelta>

To calculate with time differences.

## timedelta object

```python
datetime.timedelta(days=0, seconds=0, microseconds=0,
                   milliseconds=0, minutes=0, hours=0, weeks=0)
```             

All arguments are optional and default to 0.<br/>
Arguments may be integers or floats, and may be positive or negative.

Only days, seconds and microseconds are stored internally.<br/>
Arguments are converted to those units.

Days, seconds and microseconds are then normalized
so that the representation is unique.

## Example – add a given amount of time to a datetime object

```python
import datetime

lock_interval_hours = 2
now = datetime.datetime.now()
finish_time = (now + datetime.timedelta(hours=lock_interval_hours))
print("now        :", now)
print("finish_time:", finish_time)
```

## Example – difference between two datetime objects

The timedelta attributes can be used to get the info of a difference:

```python
datetime.timedelta.days
datetime.timedelta.seconds           # without days!!! it is an attribute
datetime.timedelta.total_seconds()   # with days       it is a method (function)
datetime.timedelta.microseconds
```

```python
import datetime

now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)
diff = tomorrow - now
print("days:", diff.days)
print("seconds:", diff.seconds)
print("total_seconds:", diff.total_seconds())
print("microseconds:", diff.microseconds)
```

TODO write about whenever  
<https://whenever.readthedocs.io/en/latest/deltas.html>
