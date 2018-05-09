# -*-coding:utf-8 -*-

'''
handle all the logging works
'''
import logging
from conf import settings

def logger(log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(settings. LOG_LEVEL)

    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
    """logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')"""

