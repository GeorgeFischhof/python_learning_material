
import create_logger


def is_debug():
    return True


def use_created_logger():
    logger = create_logger.create_logger(name='Demo_create_logger', debug=is_debug())

    logger.info('Info message')
    logger.debug('Debug message')


if __name__ == '__main__':
    use_created_logger()
