
import atexit
import logging


def create_handler(name, level, formatter):
    log_file_handler = logging.FileHandler('{name}_{level}.log'.format(name=name, level=level), mode='w')
    log_file_handler.setLevel(level.upper())
    log_file_handler.setFormatter(formatter)

    return log_file_handler


def create_multiple_file_logger(name):
    # https://docs.python.org/3/library/logging.html#logging.Logger.setLevel
    #
    # !!! NOTSET logger does not accept logs, forwards them to root logger
    # so here we have to use root logger or named logger with level 1
    # (by default root logger is not configured now, so its level is warning)
    # (info and debug messages are dropped)
    #
    # As we do not care with name of the logger and the hierarchy now
    # the usage of root logger is a good idea

    logger = logging.getLogger()  # without name we will get the root logger
    logger.setLevel(logging.NOTSET)

    log_formatter = logging.Formatter('{asctime} - {module:20} - {levelname:8} - {message}', style='{')

    log_file_debug_handler = create_handler(name, 'debug', log_formatter)
    log_file_info_handler = create_handler(name, 'info', log_formatter)
    log_file_warning_handler = create_handler(name, 'warning', log_formatter)
    log_file_error_handler = create_handler(name, 'error', log_formatter)

    logger.addHandler(log_file_debug_handler)
    logger.addHandler(log_file_info_handler)
    logger.addHandler(log_file_warning_handler)
    logger.addHandler(log_file_error_handler)

    atexit.register(logging.shutdown)

    return logger
