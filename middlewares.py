#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
class DownloaderMiddleware1(object):
    """
        下载中间件：Downloader提交给Enigma的Response，或Engine提交给Downloader的Request
    """
    def process_request(self, request, spider):
        print("[DownloaderMiddleware1] Process Reqeuest <{}>".format(request.url))
        request.headers= {
            "Host": re.findall(r'//(.*?)/',request.url)[0],
            "Referer": "https://sz.ke.com/ershoufang/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
        return request


    def process_response(self, response, spider):
        print(response.te)
        print("[DownloaderMiddleware1] Process Response <{}>".format(response.url))
        return response