#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymongo
from config import env
class MongoOperator(object):

    def __init__(self, user=None, pwd=None, db="admin", host='localhost',port=27017):
        if env == 'test':
            uri= 'mongodb://localhost:27017/'
        else:
            uri = 'mongodb://%s:%s@%s:%s/%s' % (user, pwd, host, port,db)
        self.client = pymongo.MongoClient(uri, unicode_decode_error_handler='ignore')


if __name__ == '__main__':
    a=MongoOperator()
    db=a.client['test_local']
    co = db.test_collection
    d=co.find({})
    for i in d:
        print(i)