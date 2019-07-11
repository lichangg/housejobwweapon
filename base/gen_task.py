#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests,json,re,random
from lxml import etree
from base.statu_code import Status
from utils.proxy import proxies
from retry import retry
USER_AGENTS=[
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
]
base_header = random.choice(USER_AGENTS)
def _requests(use_proxy,headers,*args,**kwargs):
    headers['user-agent']=random.choice(USER_AGENTS)
    if use_proxy:
        return requests.get(url=None,headers=headers,proxies=proxies, *args,**kwargs)
    else:
        return requests.get(url=None,headers=headers, proxies=None, *args, **kwargs)
class TaskProducer():
    requests=_requests
    json=json
    re=re
    retry=retry
    status=Status
    etree=etree
    def __init__(self, plat_name, task_mq, customer,queue):
        self._plat_name = plat_name
        self._task_mq = task_mq
        self._customer = customer
        self._queue = queue

    def crawl(self,url_data):
        pass
    @staticmethod
    def new_house_obj():
        house_obj = {}
        house_obj['city'] = None
        house_obj['title'] = None
        house_obj['loc'] = None
        house_obj['struct'] = None
        house_obj['area'] = None
        house_obj['rent'] = None
        house_obj['attr'] = None
        house_obj['community_name'] = None
        house_obj['thumb_img'] = None
        house_obj['pub_time'] = None
        house_obj['img_group'] = None
        house_obj['extra'] = None
        return house_obj



