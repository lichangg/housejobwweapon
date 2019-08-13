#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base.request import LRequest
class Spider(object):

    start_urls = []


    def start_requests(self):
        """
            返回第一个入口请求给引擎
        """
        for url in self.start_urls:
            yield LRequest(url)


    def parse(self, response):
        raise Exception("Must overwrite parse function!")
        # #content = {"content" : response.body}
        # content = response.body

        # item = Item(content)
        # return item