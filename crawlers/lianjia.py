#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base.gen_task import TaskProducer

class LianjiaCrawler(TaskProducer):
    def crawl(self, url_data):
        url = url_data.get('url')
        self.request.get(url)