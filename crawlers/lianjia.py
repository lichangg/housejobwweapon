#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base.gen_task import TaskProducer


class LianjiaCrawler(TaskProducer):
    def crawl(self, url_data):
        url = url_data.get('url')
        self.requests.get(url)


if __name__ == '__main__':
    import requests

    domain = 'https://sz.lianjia.com'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "sz.lianjia.com",
        "Pragma": "no-cache",
        "Referer": "https://sz.lianjia.com/?utm_source=baidu&utm_medium=pinzhuan&utm_term=biaoti&utm_content=biaotimiaoshu&utm_campaign=sousuo",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    }
    resp = requests.get(domain + '/zufang/shuixiechuntian/', headers=headers)
    from lxml import etree

    dom = etree.HTML(resp.text)
    house_doms = dom.xpath('//div[@class="content__list--item"]')
    for house_dom in house_doms:
        city = house_dom.xpath('//h1/a/text()')
        loc = house_dom.xpath('.//p[@class="content__list--item--des"]//a/text()')
        title = house_dom.xpath('.//p[@class="content__list--item--title twoline"]//a/text()')
        url = house_dom.xpath('.//p[@class="content__list--item--title twoline"]//a/@href')
        struct = house_dom.xpath('.//p[@class="content__list--item--des"]/text()')
        # area =dom.xpath('')
        rent = house_dom.xpath('.//span[@class="content__list--item-price"]/em/text()')
        attr = house_dom.xpath('.//p[@class="content__list--item--bottom oneline"]//i/text()')
        thumb_img = house_dom.xpath('.//a[@class="content__list--item--aside"]/img/@src')
        pub_time = house_dom.xpath('.//p[@class="content__list--item--time oneline"]/text()')

        house_obj = dict()
        house_obj['city'] = city[0].replace('深圳', '')
        house_obj['title'] = title[0].strip()
        house_obj['house_url'] = domain + url[0]
        house_obj['district'] = loc[0]
        house_obj['loc'] = '-'.join(loc)
        house_obj['struct'] = '-'.join([i.strip() for i in struct]).strip('-')
        house_obj['area'] = house_obj['struct'].split('-')[0]
        house_obj['rent'] = rent[0]
        house_obj['attr'] = attr
        house_obj['community_name'] = house_obj['title'].split(' ')[0].replace('整租·', '').replace('合租·', '')
        house_obj['thumb_img'] = thumb_img[0]
        house_obj['pub_time'] = pub_time[0]
        house_obj['extra'] = None
        print(house_obj)
