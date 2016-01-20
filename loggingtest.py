#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# loggingtest.py - тестирование логирования с Rotating handlers
#


import logging
import logging.handlers
import sys

dateFormat = '%a, %d %b %Y %H:%M:S'
fileFormat = '[%(asctime)s %(process)d] %(levelname)s (%(module)s:%(lineno)d %(message)s)'
streamFormat = '%(asctime)s %(levelname)-8s %(message)s'
filename = 'test.log'

rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
fileHandler = logging.handlers.RotatingFileHandler(filename,
                                                    maxBytes=1024, backupCount=5)
fileHandler.setFormatter(logging.Formatter(fileFormat, dateFormat))
rootLogger.addHandler(fileHandler)
streamHandler = logging.StreamHandler(sys.stderr)
streamHandler.setFormatter(logging.Formatter(streamFormat, dateFormat))
rootLogger.addHandler(streamHandler)

rootLogger.info("Hello! I'm rootLogger message!")
