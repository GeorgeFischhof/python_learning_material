# Time

<https://docs.python.org/3/library/time.html>

The most valuable functions

## time.time()

Returns the seconds since epoch (1970.01.01 00:00:00 UTC)
as a float (with 6–7 decimals).

## time.perf_counter()  time.perf_counter_ns()

<https://docs.python.org/3/library/time.html#time.perf_counter>

`time.perf_counter()`
> Return the value (in fractional seconds) of a performance counter, i.e. a clock with the highest available resolution
> to measure a short duration. It does include time elapsed during sleep. The clock is the same for all processes. The
> reference point of the returned value is undefined, 
> so that only the difference between the results of two calls is valid.
> Use `perf_counter_ns()` to avoid the precision loss caused by the float type.

`time.perf_counter_ns()`
> Similar to `perf_counter()`, but return time as nanoseconds.

## time.sleep(time_in_seconds)

Waits `time_in_seconds` seconds (int or float).
