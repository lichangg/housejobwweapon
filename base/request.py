#!/usr/bin/env python
# -*- coding:utf-8 -*-
class LRequest(object):
    """
        请求类，方便传递一些额外参数
    """
    def __init__(self, url, method="GET", headers=None, params=None, formdata=None, proxies=None, callback="parse", dont_filter=False, use_sess=False,extra=None,timeout=None):
        self.url = url
        self.method = method
        self.headers = headers
        self.params = params    # 查询字符串
        self.formdata = formdata    # 表单数据
        self.proxies = proxies
        self.callback = callback
        self.dont_filter = dont_filter # 是否去重
        self.use_sess = use_sess # 是否使用session
        self.extra = extra
        self.timeout = timeout

    def __str__(self):
        return f'本次请求信息:url为{self.url},代理为{self.proxies},表单数据为{str(self.formdata)}'