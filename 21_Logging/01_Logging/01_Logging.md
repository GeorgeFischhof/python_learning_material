# Logging

<https://docs.python.org/3/howto/logging.html>
<https://docs.python.org/3/library/logging.html>

<https://realpython.com/python-logging/>

## Logging is a very useful tool in a programmer’s toolbox

It can help you develop a better understanding of what happens
and when during the running of your program. <br/>
(debug logging) <br/>
You can use it instead of printing values,
and it can be turned off with a simple setting (no debug logging).

It can help you inform the user about special events. <br/>
Or in case of serious events,
warnings and error messages can be emitted to the user.

And of course these events (from debug to business point of view)
can be written to file.  <br/>
(debug and forensics can be among the purposes)

## The logging system is hierarchical (by name)

Therefore the logging of an imported submodule can
appear between the importer’s logs,
and they can be accessed or turned off.

Of course the logging of the submodule must be written in a way that enables this behaviour. <br/>
(See logging in multiple modules and logging in library)

## Log flow (simplified)

```
call ==>
  log level filter ==>
    log filter ==>
      handler ==>
        log level filter ==>
          log filter ==>
            parent logger (if exists) ==> back to parent's handler (hierarchy)
            formatter ==> write out
```

## Log levels

```
Level       Numeric value

CRITICAL    50
ERROR       40
WARNING     30  (default)
INFO        20
DEBUG       10
NOTSET      0
```

## Start logging

A log record has
- level
- message
- format
- time format
- module info
- function info
- logger name (given name, or module name, or root)

## There are two ways to start logging

1.  Use the logging module’s methods.
    It is simple, because these methods use the default logger,
    which has a formatter too. <br/>
    (But the default level is still warning...)

```python
import logging
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
# == >
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message
```

2.  Get and use a logger object. (It is configurable.) <br/>
    Optional name identifies the logger; if no name is passed,
    then it will be called `root`. <br/>
    This object does NOT use any defaults, neither does it have any formatter. <br/>
    (The default level is still warning...)

```python
import logging
logger = logging.getLogger("name to identify")  # you can change the name if you want

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
# ==>
# This is a warning message
# This is an error message
# This is a critical message
```

## Shutting down the logging subsystem

```python
import atexit
atexit.register(logging.shutdown)
```

## Notes on filter

<https://docs.python.org/3/library/logging.html#filter-objects>
<https://docs.python.org/3/howto/logging-cookbook.html#using-filters-to-impart-contextual-information>

Filters are functions that we have to implement which process the log record.<br/>
If it returns a non-zero or True value, then the record will go further on its way.<br/>
Otherwise the record is dropped.

The filter can add additional information to the record before letting it go further.


TODO: add loguru
