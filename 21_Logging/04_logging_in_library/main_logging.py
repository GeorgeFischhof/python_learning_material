
import atexit
import logging

import library


def create_logger():
    log_formatter = logging.Formatter('{asctime} - {module:20} - {levelname:8} - {message}', style='{')

    log_console_handler = logging.StreamHandler()  # default is sys.stderr
    log_console_handler.setLevel(logging.INFO)
    log_console_handler.setFormatter(log_formatter)

    module_logger = logging.getLogger('main')
    module_logger.setLevel(logging.INFO)
    module_logger.addHandler(log_console_handler)

    atexit.register(logging.shutdown)

    return module_logger


def do_logging():
    logger.debug('Main module debug')
    logger.info('Main module info')
    logger.warning('Main module warning')
    logger.error('Main module error')
    logger.critical('Main module critical \n')

    library.do_logging()


if __name__ == '__main__':
    logger = create_logger()
    do_logging()
