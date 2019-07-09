#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import os
from logging.handlers import RotatingFileHandler

loggerLevel = logging.INFO
root_path = os.getcwd().split('housejobwweapon')[0] + 'housejobwweapon'
log_dir = root_path + '/logs'
console_formatter = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
json_formatter = '%(message)s'
logger_dict = dict()


def create_logger(log_name, log_type):
    g_logger = logging.getLogger(log_name)
    rt = log_name.split('_')[0]
    log_path = "%s/%s" % (log_dir, rt)
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logfile = log_name + ".log"
    log_file = "%s/%s" % (log_path, logfile)
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter(console_formatter))
    handler = RotatingFileHandler(log_file, maxBytes=2 * 1204 * 1024, backupCount=1)
    fmt = json_formatter if log_type == 'json' else console_formatter
    handler.setFormatter(logging.Formatter(fmt))
    g_logger.addHandler(console)
    g_logger.addHandler(handler)
    g_logger.setLevel(loggerLevel)
    return g_logger


def get_logger(log_name, log_type='file'):
    if log_name not in logger_dict:
        create_logger(log_name, log_type)
        logger_dict[log_name] = logging.getLogger(log_name)
    return logging.getLogger(log_name)
