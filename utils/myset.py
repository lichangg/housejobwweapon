#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .default_settings import *

# python set : add()  if in
# redis set:  sadd()  sismember()


import redis

class BaseFilterSet(object):
    def add_fp(self, fp):
        pass

    def is_filter(self, fp):
        pass


class NormalFilterSet(BaseFilterSet):
    def __init__(self):
        self._filter_set = set()

    def add_fp(self, fp):
        self._filter_set.add(fp)

    def is_filter(self, fp):
        # 判断指纹是否在集合中，如果在返回True，否则返回False
        return True if fp in self._filter_set else False



class RedisFilterSet(BaseFilterSet):

    def __init__(self):
        self._filter_set = redis.Redis(host=REDIS_QUEUE_HOST, port=REDIS_QUEUE_PORT, db=REDIS_QUEUE_DB)
        self._set_name = REDIS_QUEUE_NAME

    def add_fp(self, fp):
        self._filter_set.sadd(self._set_name, fp)


    def is_filter(self, fp):
        # 判断指纹是否在集合中，如果在返回True，否则返回False
        return self._filter_set.sismember(self._set_name, fp)