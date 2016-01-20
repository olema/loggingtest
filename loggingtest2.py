#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import logging.handlers


LOG_FILENAME = 'test2.log'

dateformat = '%Y-%m-%d %H:%M:%S'
fileformat = '[%(asctime)s] %(levelname)s: %(message)s'


my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=100, backupCount=5)
handler.setFormatter(logging.Formatter(fileformat, dateformat))
my_logger.addHandler(handler)

my_logger.info('Hello!')
