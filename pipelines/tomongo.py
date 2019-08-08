#!/usr/bin/env python
# -*- coding:utf-8 -*-
class SaveToMongoPipeline(object):
    def process_item(self, item):
        print("[Pipeline]: item data : {}".format(item.data))
        return item