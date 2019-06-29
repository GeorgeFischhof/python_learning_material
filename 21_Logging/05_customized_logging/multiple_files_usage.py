
import multiple_files


def use_multiple_files_logger():
    logger = multiple_files.create_multiple_file_logger(name='Z_Demo_multiple_files_logger')

    # we can override the level of the logger
    # logger.setLevel('WARNING')

    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')


if __name__ == '__main__':
    use_multiple_files_logger()
