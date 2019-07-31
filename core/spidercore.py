#!/usr/bin/env python
# -*- coding:utf-8 -*-
SPIDERS = ['beike.BeikeCrawler',
           'lianjia.LianjiaCrawler',
           'mogu.MoguCrawler']
class Core():
    # def __init__(self, spider_group, task_gettter):
    #     # self.spider_group = spider_group
    #     # self.task_getter = task_gettter
    #     self.spiders=self._auto_import_cls(SPIDERS,True)
    def _auto_import_cls(self, path_list=[], is_spider=False):
        if is_spider:
            instances = {}
        else:
            instances = []

        import importlib

        for path in path_list:
            module_name = 'crawlers.'+path[:path.rfind(".")]
            class_name = path[path.rfind(".") + 1:]
            result = importlib.import_module(module_name)
            cls = getattr(result, class_name)

            if is_spider:
                instances[cls.name] = cls()
                print(f'爬虫“{cls.name}”已加载')

            else:
                instances.append(cls())
        return instances

if __name__ == '__main__':
    a=Core()


    s=a._auto_import_cls(SPIDERS,True)
    print(s)