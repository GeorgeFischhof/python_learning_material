
import logging


def create_logger():

    log_null_handler = logging.NullHandler()
    log_null_handler.setLevel(logging.DEBUG)

    library_logger = logging.getLogger("main.library")  # in a normal package __name__ is used
    library_logger.setLevel(logging.DEBUG)
    library_logger.addHandler(log_null_handler)

    return library_logger


def do_logging():
    logger.debug("Library debug")
    logger.info("Library info")
    logger.warning("Library warning")
    logger.error("Library error")
    logger.critical("Library critical")


logger = create_logger()
