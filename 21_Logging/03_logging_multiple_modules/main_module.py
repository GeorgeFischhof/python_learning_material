
# import atexit  # from Python 3.8 logging.shutdown is automatic
import logging

import sub_module


# logging.disable(logging.ERROR)  # disable logs UP TO level

# logging.getLogger("main_module.sub_module").disabled = True  # turn off logging of the given sublogger

def create_logger():
    log_formatter = logging.Formatter("{asctime} - {module:20} - {levelname:8} - {message}", style="{")

    log_console_handler = logging.StreamHandler()  # default is sys.stderr
    log_console_handler.setLevel(logging.INFO)
    log_console_handler.setFormatter(log_formatter)

    module_logger = logging.getLogger("main_module")  # Hierarchical name
    module_logger.setLevel(logging.INFO)
    module_logger.addHandler(log_console_handler)

    # atexit.register(logging.shutdown)  # from Python 3.8 logging.shutdown is automatic

    return module_logger


def do_logging():
    logger.debug("Main module debug")
    logger.info("Main module info")
    logger.warning("Main module warning")
    logger.error("Main module error")
    logger.critical("Main module critical \n")

    sub_module.do_logging()


if __name__ == "__main__":
    logger = create_logger()
    do_logging()
