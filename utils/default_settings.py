#!/usr/bin/env python
# -*- coding:utf-8 -*-


SPIDERS = [
]


PIPELINES = [
]

SPIDER_MIDDLEWARES = [
]

DOWNLOADER_MIDDLEWARES = [
]
REDIS_QUEUE_NAME='request_queue'
REDIS_QUEUE_HOST='127.0.0.1'
REDIS_QUEUE_PORT='6379'
REDIS_QUEUE_DB=0
ASYNC_COUNT = 5
ASYNC_TYPE = 'thread'
ROLE=None
try:
    # 表示执行用户代码目录下的settings
    from settings import *
except:
    pass
