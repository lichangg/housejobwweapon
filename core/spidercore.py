#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from concurrent.futures import as_completed
from datetime import datetime

from base.requestexec import BaseThreadPoolExecutor
from traceback import format_exc
from core.downloader import Downloader
from core.scheduler import Scheduler
from base.request import LRequest
# from base.response import LResponse
from base.item import Item
from utils.default_settings import *
from settings import *
from base.exceptions import *
if ASYNC_TYPE == "thread":
    from multiprocessing.dummy import Pool
    print("[并发类型]: {}".format(ASYNC_TYPE))

elif ASYNC_TYPE == "coroutine":
    from utils.asyncpool import Pool
    print("[并发类型]: {}".format(ASYNC_TYPE))

else:
    raise Exception("Not Support Async Type: {}".format(ASYNC_TYPE))


class Core():
    def __init__(self):#, spider_group, task_gettter):
        # self.spider_group = spider_group
        # self.task_getter = task_gettter
        self.spiders=self._auto_import_cls(SPIDERS,True)
        self.pool = Pool()
        self.pipelines = self._auto_import_cls(PIPELINES)
        self.spider_mids = self._auto_import_cls(SPIDER_MIDDLEWARES)
        #self.downloader_mids = downloader_mids
        self.downloader_mids = self._auto_import_cls(DOWNLOADER_MIDDLEWARES)
        self.scheduler = Scheduler(ROLE,QUEUE_TYPE)
        self.downloader = Downloader()
        # self.spider_mids = spider_mids
        self.spider_mids = self._auto_import_cls(SPIDER_MIDDLEWARES)
        self.is_running = True
        self.total_response = 0
        self.executor = BaseThreadPoolExecutor(max_workers=ASYNC_COUNT)
    def _auto_import_cls(self, path_list=[], is_spider=False):
        if is_spider:
            instances = {}
        else:
            instances = []

        import importlib

        for path in path_list:


            if is_spider:
                module_name = 'crawlers.' + path[:path.rfind(".")]
                class_name = path[path.rfind(".") + 1:]
                result = importlib.import_module(module_name)
                cls = getattr(result, class_name)
                instances[cls.name] = cls()
                print(f'爬虫“{cls.name}”已加载')

            else:
                module_name = path[:path.rfind(".")]
                class_name = path[path.rfind(".") + 1:]
                result = importlib.import_module(module_name)
                cls = getattr(result, class_name)
                instances.append(cls())
                print(f'“{cls.__name__}”已加载')
        return instances
    def _start_engine(self):
        # master只执行 添加请求，所以total_request会自增，
        # 但是不发送请求total_response不会自增
        if ROLE == "master" or ROLE is None:
            # 将Engine的工作分工，分为两部分：
            # 1 处理start_request请求并存如调度器中
            #self._execute_start_requests()
            self.pool.apply_async(self._execute_start_requests)

        while 1:
            time.sleep(0.01)
            li_req = self.scheduler.get_batch_requests(ASYNC_COUNT)
            if not li_req:
                continue
            tasks = [self.executor.submit(self._execute_request_return_item,req) for req in li_req]
            for fu in as_completed(tasks):
                fu.result()
            if self.scheduler.total_request == self.total_response and self.scheduler.total_request != 0:
                self.is_running = False
                break
        print("Main Thread is over!")
    # def _callback(self, _):
    #     if self.is_running:
    #         self.pool.apply_async(self._execute_request_response_item, callback=self._callback)
    def start(self):
        # 开始时间
        start = datetime.now()
        print("Start time : {}".format(start))
        print("----"*30)

        self._start_engine()

        # 结束时间
        end = datetime.now()

        print("----"*30)
        print("End time : {}".format(end))
        # 总计运行时间
        print("Useing time : {}".format( (end - start).total_seconds() ))

    def _execute_start_requests(self):
        # 将所有爬虫的start_urls里的请求全部放入同一个调度器中
        #[("baidu", baidu_spider), ("douban" : douban_spider)]
        for spider_name, spider in self.spiders.items():
            print(spider_name, spider)
            # 1. 从spider中获取第一批请求，交给调度器
            #request = self.spider.start_requests()
            for request in spider.start_requests():
                # 第一次处理请求时，就添加爬虫名，该爬虫名可以传递到后续提取的请求中
                request.spider_name = spider_name
                # 1.1 将请求交给spider中间件做处理，再返回处理后的请求
                for spider_mid in self.spider_mids:
                    request  = spider_mid.process_request(request, spider)

                self.scheduler.add_request(request)


    def _execute_request_response_item(self):
        # 每次while 循环，处理的都是同一个爬虫下的某一个请求
        #while True:
        # 2. 取出调度器的请求，并交给下载器，下载器返回响应交给spider解析
        request = self.scheduler.get_request()

        if not request:
            #break
            return

        # 获取请求对应的爬虫对象
        spider = self.spiders[request.spider_name]

        # 2.1 将调度器中返回的请求交给下载中间件做预处理，并返回处理后的请求
        for downloader_mid in self.downloader_mids:
            request = downloader_mid.process_request(request, spider)

        response = self.downloader.send_request(request)
        # 2.2 将下载器返回的响应交给下载中间件做预处理，并返回处理后的响应
        for downloader_mid in self.downloader_mids:
            response = downloader_mid.process_response(response, spider)
        #  将响应交给爬虫解析
        # parse_func = spider.parse(response)

        #爬虫对象的某个解析方法 parse， parse_page
        #getattr(spider, "parse_page")
        # 动态获取获取爬虫对象的该请求指定的回调函数，并将响应传入回调函数解析



        callback_func = getattr(spider, request.callback)
        parse_func = callback_func(response)




        for item_or_request in parse_func:
            # 3. 判断解析结果，如果是请求继续交给调度器；如果是item数据交给管道
            if isinstance(item_or_request, LRequest):
                item_or_request.spider_name = spider.name

                for spider_mid in self.spider_mids:
                    item_or_request  = spider_mid.process_request(item_or_request, spider)

                self.scheduler.add_request(item_or_request)

            elif isinstance(item_or_request, Item):
                for spider_mid in self.spider_mids:
                    item_or_request = spider_mid.process_item(item_or_request, spider)

                for pipeline in self.pipelines:
                    item_or_request = pipeline.process_item(item_or_request, spider)
            else:
                raise Exception("Not support data type : <{}>".format(type(item_or_request)))


        self.total_response += 1
    def _execute_request_return_item(self,request:LRequest):

        if not request:
            return

        spider = self.spiders[request.spider_name]

        for downloader_mid in self.downloader_mids:
            request = downloader_mid.process_request(request, spider)
        try:
            response = self.downloader.send_request(request)
        except Exception as e:
            spider.logger.error(f'链接{request.url}出错：'+str(e))
            return
        for downloader_mid in self.downloader_mids:
            response = downloader_mid.process_response(response, spider)

        callback_func = getattr(spider, request.callback)
        try:
            parse_func = callback_func(response)
            for item_or_request in parse_func:
                if isinstance(item_or_request, LRequest):
                    item_or_request.spider_name = spider.name

                    for spider_mid in self.spider_mids:
                        item_or_request  = spider_mid.process_request(item_or_request, spider)

                    self.scheduler.add_request(item_or_request)

                elif isinstance(item_or_request, Item):
                    for spider_mid in self.spider_mids:
                        item_or_request = spider_mid.process_item(item_or_request, spider)

                    for pipeline in self.pipelines:
                        item_or_request = pipeline.process_item(item_or_request, spider)
                else:
                    raise Exception("Not support data type : <{}>".format(type(item_or_request)))
        except Exception as e:
            spider.logger.error(f'解析{request.url}出错：'+str(e)+f'响应码[{response.status_code}]')
            return
        self.total_response += 1
if __name__ == '__main__':
    a=Core()


    s=a._auto_import_cls(SPIDERS,True)
    print(s)