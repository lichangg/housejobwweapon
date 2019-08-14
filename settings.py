#!/usr/bin/env python
# -*- coding:utf-8 -*-
DOWNLOADER_MIDDLEWARES=['middlewares.DownloaderMiddleware1']
PIPELINES=['pipelines.HousePipeline']
MONGO_HOST='127.0.0.1'
SPIDERS = ['beike.BeikeCrawler']
           # 'lianjia.LianjiaCrawler',
           # 'mogu.MoguCrawler']

ASYNC_COUNT=5