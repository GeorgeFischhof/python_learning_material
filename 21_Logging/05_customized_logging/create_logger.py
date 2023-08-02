
# import atexit  # needed before Python 3.8
import logging


def create_logger(name, debug=False):
    logger = logging.getLogger(name)  # we can use the root logger as well if we omit the name

    log_formatter = logging.Formatter('{asctime} - {module:20} - {levelname:8} - {message}', style='{')

    if debug:
        log_file_handler = logging.FileHandler('Z_{name}_debug.log'.format(name=name), mode='w')
        log_file_handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
    else:
        log_file_handler = logging.FileHandler('Z_{name}.log'.format(name=name), mode='w')
        log_file_handler.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)

    log_file_handler.setFormatter(log_formatter)

    logger.addHandler(log_file_handler)

    # atexit.register(logging.shutdown)  # needed before Python 3.8
    # https://docs.python.org/3.8/library/logging.html#logging.shutdown

    return logger
