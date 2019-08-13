#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import chardet
from traceback import format_exc
from base.response import LResponse
from retry import retry
# from ..utils.log import logger

class Downloader(object):
    @retry(tries=3)
    def send_request(self, request):
        print("[Downloader] : Request [{}] <{}>".format(request.method, request.url))
        print('注意',request.url)
        print('注意',request.headers)
        if request.method.upper() == "GET":
            try:
                response = requests.get(
                    url = request.url,
                    headers = request.headers,
                    params = request.params,
                    proxies = request.proxies,
                    timeout = request.timeout

                )
            except Exception as e:
                print(format_exc())
                raise e
        elif request.method.upper() == "POST":
            try:
                response = requests.post(
                    url = request.url,
                    headers = request.headers,
                    data = request.formdata,
                    proxies = request.proxy

                )
            except Exception as e:
                print(format_exc())
                raise e
        else:
            # 如果请求方法不支持，则抛出异常
            raise Exception("Not Support method <{}>".format(request.method))

        print("[Downloader]: Response [{}] <{}>".format(response.status_code, response.url))

        # 构建响应对象，返回给引擎
        return LResponse(
                url = response.url,
                body = response.content,
                #text = response.content.decode(chardet.detect(response.content)['encoding']),
                text = "",
                headers = response.headers,
                status_code = response.status_code,
                encoding = chardet.detect(response.content)['encoding'],
                request = request,
                extra = request.extra,
        )

if __name__ == '__main__':
    from base.request import LRequest
    headers = {
               "Host": "sz.zu.ke.com",
               "Referer": "https://sz.ke.com/ershoufang/",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    domain='https://sz.zu.ke.com'
    url = 'https://sz.zu.ke.com/zufang/pg2'
    r = LRequest(url=url,headers=headers)
    resp = Downloader().send_request(r)
    print(resp.text)
    '''
    注意 https://sz.zu.ke.com/zufang/pg2
    注意 {'Host': 'sz.zu.ke.com', 'Referer': 'https://sz.ke.com/ershoufang/', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
'''
    '''
    注意 https://sz.zu.ke.com/zufang/pg0
    注意 {'Host': 'sz.zu.ke.com/zufang/pg0', 'Referer': 'https://sz.ke.com/ershoufang/', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
'''