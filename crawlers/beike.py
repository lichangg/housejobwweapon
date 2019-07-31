#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base.gen_task import TaskProducer


class BeikeCrawler():
    name = 'beike'
    def crawl(self, url_data):
        ori_url = url_data.get('url')
        page = url_data.get('page')
        url = ori_url+ f'/zufang/pg{page}'
        headers = {
            "Host": ori_url.replace('https://', ''),
            "Referer": "https://sz.ke.com/ershoufang/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

        resp = self.requests.get(url, headers=headers)
        dom = self.etree.HTML(resp.text)
        house_doms = dom.xpath('//div[@class="content__list--item"]')
        house_li = []
        for house_dom in house_doms:
            loc = house_dom.xpath('.//p[@class="content__list--item--des"]//a/text()')
            title = house_dom.xpath('.//p[@class="content__list--item--title twoline"]//a/text()')
            url = house_dom.xpath('.//p[@class="content__list--item--title twoline"]//a/@href')
            rent = house_dom.xpath('.//span[@class="content__list--item-price"]//em/text()')
            struct = house_dom.xpath('.//p[@class="content__list--item--des"]/text()')
            attr = house_dom.xpath('.//p[@class="content__list--item--bottom oneline"]//i/text()')
            thumb_img = house_dom.xpath('.//a[@class="content__list--item--aside"]//img/@data-src')
            pub_time = house_dom.xpath('.//p[@class="content__list--item--time oneline"]/text()')

            house_obj = dict()
            house_obj['title'] = title[0].strip()
            house_obj['house_url'] = ori_url + url[0]
            house_obj['district'] = loc[0]
            house_obj['loc'] = '-'.join(loc[1:])
            house_obj['struct'] = '-'.join([i.strip() for i in struct]).strip('-')
            house_obj['area'] = house_obj['struct'].split('-')[0]
            house_obj['rent'] = rent[0]
            house_obj['attr'] = attr
            house_obj['community_name'] = loc[-1]
            house_obj['thumb_img'] = thumb_img[0]
            house_obj['pub_time'] = pub_time[0]
            house_obj['img_group'] = []
            house_obj['extra'] = None
            house_li.append(house_obj)
        return house_li
if __name__ == '__main__':
    import requests

    headers = {
               "Host": "sz.zu.ke.com",
               "Referer": "https://sz.ke.com/ershoufang/",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    domain='https://sz.zu.ke.com'
    url = 'https://sz.zu.ke.com/zufang'
    resp = requests.get(url,headers=headers)
    from lxml import etree
    dom = etree.HTML(resp.text)
    house_doms = dom.xpath('//div[@class="content__list--item"]')
    for house_dom in house_doms:
        # city= dom.xpah
        loc= house_dom.xpath('.//p[@class="content__list--item--des"]//a/text()')
        title=house_dom.xpath('.//p[@class="content__list--item--title twoline"]//a/text()')
        url=house_dom.xpath('.//p[@class="content__list--item--title twoline"]//a/@href')
        # struct=house_dom.xpath('.//p[@class="content__list--item--des"]//a/text()')
        rent=house_dom.xpath('.//span[@class="content__list--item-price"]//em/text()')
        struct=house_dom.xpath('.//p[@class="content__list--item--des"]/text()')
        attr=house_dom.xpath('.//p[@class="content__list--item--bottom oneline"]//i/text()')
        thumb_img=house_dom.xpath('.//a[@class="content__list--item--aside"]//img/@data-src')
        pub_time =house_dom.xpath('.//p[@class="content__list--item--time oneline"]/text()')

        house_obj = dict()
        # house_obj['city'] = city[0].replace('深圳', '')
        house_obj['title'] = title[0].strip()
        house_obj['house_url'] = domain + url[0]
        house_obj['district'] = loc[0]
        house_obj['loc'] = '-'.join(loc[1:])
        house_obj['struct'] = '-'.join([i.strip() for i in struct]).strip('-')
        house_obj['area'] = house_obj['struct'].split('-')[0]
        house_obj['rent'] = rent[0]
        house_obj['attr'] = attr
        house_obj['community_name'] = loc[-1]
        house_obj['thumb_img'] = thumb_img[0]
        house_obj['pub_time'] = pub_time[0]
        house_obj['img_group'] = []
        house_obj['extra'] = None
        print(house_obj)
