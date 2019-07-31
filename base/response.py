#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import json
from lxml import etree

class LResponse(object):
    """
        响应类
    """
    def __init__(self, url, body, text, headers, status_code, encoding, request):
        self.url = url  # 对应的url地址
        self.body = body
        self.text = text
        self.headers = headers
        self.status_code = status_code
        self.encoding = encoding
        self.request = request  # 对应的请求对象


    def xpath(self, rule):
        html_obj = etree.HTML(self.body)
        return html_obj.xpath(rule)

    @property
    def json(self):
        try:
            return json.loads(self.body)
        except Exception as e:
            raise e
