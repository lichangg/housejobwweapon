#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymongo
from settings import *
class HousePipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(host=MONGO_HOST)
    def process_item(self,item, spider):
        # data=dict(item)
        self.conn['housejobweapon']['house'].update({"house_code":item.data['house_code']},item.data,upsert=True)
        print(item.data,'已加入')
        return item
    def __del__(self):
        self.conn.close()