#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

from base.gen_task import TaskProducer
from base.item import Item
from base.request import LRequest
li=[{'cname': '北京', 'curl': 'https://bj.ke.com'}, {'cname': '上海', 'curl': 'https://sh.ke.com'}, {'cname': '广州', 'curl': 'https://gz.ke.com'}, {'cname': '深圳', 'curl': 'https://sz.ke.com'}, {'cname': '成都', 'curl': 'https://cd.ke.com'}, {'cname': '合肥', 'curl': 'https://hf.ke.com'}, {'cname': '北京', 'curl': 'https://bj.ke.com'}, {'cname': '重庆', 'curl': 'https://cq.ke.com'}, {'cname': '福州', 'curl': 'https://fz.ke.com'}, {'cname': '厦门', 'curl': 'https://xm.ke.com'}, {'cname': '泉州', 'curl': 'https://quanzhou.ke.com'}, {'cname': '广州', 'curl': 'https://gz.ke.com'}, {'cname': '深圳', 'curl': 'https://sz.ke.com'}, {'cname': '东莞', 'curl': 'https://dg.ke.com'}, {'cname': '贵阳', 'curl': 'https://gy.ke.com'}, {'cname': '郑州', 'curl': 'https://zz.ke.com'}, {'cname': '武汉', 'curl': 'https://wh.ke.com'}, {'cname': '长沙', 'curl': 'https://cs.ke.com'}, {'cname': '南京', 'curl': 'https://nj.ke.com'}, {'cname': '苏州', 'curl': 'https://su.ke.com'}, {'cname': '上海', 'curl': 'https://sh.ke.com'}, {'cname': '济南', 'curl': 'https://jn.ke.com'}, {'cname': '成都', 'curl': 'https://cd.ke.com'}, {'cname': '西安', 'curl': 'https://xa.ke.com'}, {'cname': '天津', 'curl': 'https://tj.ke.com'}, {'cname': '杭州', 'curl': 'https://hz.ke.com'}, {'cname': '宁波', 'curl': 'https://nb.ke.com'}]

beike_urls=[i['']for i in li

class BeikeCrawler():
    name = 'beike'
    c_map = {'https://bj.ke.com': '北京', 'https://sh.ke.com': '上海', 'https://gz.ke.com': '广州', 'https://sz.ke.com': '深圳', 'https://cd.ke.com': '成都', 'https://hf.ke.com': '合肥', 'https://cq.ke.com': '重庆', 'https://fz.ke.com': '福州', 'https://xm.ke.com': '厦门', 'https://quanzhou.ke.com': '泉州', 'https://dg.ke.com': '东莞', 'https://gy.ke.com': '贵阳', 'https://zz.ke.com': '郑州', 'https://wh.ke.com': '武汉', 'https://cs.ke.com': '长沙', 'https://nj.ke.com': '南京', 'https://su.ke.com': '苏州', 'https://jn.ke.com': '济南', 'https://xa.ke.com': '西安', 'https://tj.ke.com': '天津', 'https://hz.ke.com': '杭州', 'https://nb.ke.com': '宁波'}


    def start_requests(self):
        for beike_url in self.c_map:
            'https://bj.zu.ke.com/zufang/pg2'
            url = beike_url.split('.')[0]+'.zu.'+'.'.join(beike_url.split('.')[:])

            # query_url = re.findall(r'(https://.*?/)',url)[0]
            yield LRequest(url, dont_filter=True,extra=self.c_map[beike_url])
        # yield 'https://sz.zu.ke.com/zufang/pg1'
    # def crawl(self, url_data):
    #     ori_url = url_data.get('url')
    #     page = url_data.get('page')
    #     url = ori_url+ f'/zufang/pg{page}'
    #     headers = {
    #         "Host": ori_url.replace('https://', ''),
    #         "Referer": "https://sz.ke.com/ershoufang/",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    #
    #     resp = self.requests.get(url, headers=headers)
    #     dom = self.etree.HTML(resp.text)
    #     house_doms = dom.xpath('//div[@class="content__list--item"]')
    #     house_li = []
    #     for house_dom in house_doms:
    #         loc = house_dom.xpath('.//p[@class="content__list--item--des"]//a/text()')
    #         title = house_dom.xpath('.//p[@class="content__list--item--title twoline"]//a/text()')
    #         url = house_dom.xpath('.//p[@class="content__list--item--title twoline"]//a/@href')
    #         rent = house_dom.xpath('.//span[@class="content__list--item-price"]//em/text()')
    #         struct = house_dom.xpath('.//p[@class="content__list--item--des"]/text()')
    #         attr = house_dom.xpath('.//p[@class="content__list--item--bottom oneline"]//i/text()')
    #         thumb_img = house_dom.xpath('.//a[@class="content__list--item--aside"]//img/@data-src')
    #         pub_time = house_dom.xpath('.//p[@class="content__list--item--time oneline"]/text()')
    #
    #         house_obj = dict()
    #         house_obj['title'] = title[0].strip()
    #         house_obj['house_url'] = ori_url + url[0]
    #         house_obj['district'] = loc[0]
    #         house_obj['loc'] = '-'.join(loc[1:])
    #         house_obj['struct'] = '-'.join([i.strip() for i in struct]).strip('-')
    #         house_obj['area'] = house_obj['struct'].split('-')[0]
    #         house_obj['rent'] = rent[0]
    #         house_obj['attr'] = attr
    #         house_obj['community_name'] = loc[-1]
    #         house_obj['thumb_img'] = thumb_img[0]
    #         house_obj['pub_time'] = pub_time[0]
    #         house_obj['img_group'] = []
    #         house_obj['extra'] = None
    #         house_li.append(house_obj)
    #     return house_li
    def parse(self,response):
        ori_url = response.url
        house_doms = response.xpath('//div[@class="content__list--item"]')
        for house_dom in house_doms:
            loc = house_dom.xpath('.//p[@class="content__list--item--des"]//a/text()')
            title = house_dom.xpath('.//p[@class="content__list--item--title twoline"]//a/text()')
            url = house_dom.xpath('.//p[@class="content__list--item--title twoline"]//a/@href')
            rent = house_dom.xpath('.//span[@class="content__list--item-price"]//em/text()')
            struct = house_dom.xpath('.//p[@class="content__list--item--des"]/text()')
            attr = house_dom.xpath('.//p[@class="content__list--item--bottom oneline"]//i/text()')
            thumb_img = house_dom.xpath('.//a[@class="content__list--item--aside"]//img/@data-src')
            pub_time = house_dom.xpath('.//p[@class="content__list--item--time oneline"]/text()')
            pn_house_code = house_dom.xpath('./@data-house_code')

            house_obj = dict()
            house_obj['title'] = title[0].strip()
            house_obj['house_code'] = pn_house_code[0]
            house_obj['house_url'] = ori_url + url[0]
            house_obj['district'] = loc[0]
            house_obj['loc'] = '-'.join(loc[1:])
            house_obj['struct'] = '-'.join([i.strip() for i in struct]).strip('-')
            house_obj['area'] = house_obj['struct'].split('-')[0]
            house_obj['rent'] = float(rent[0])
            house_obj['attr'] = attr
            house_obj['community_name'] = loc[-1]
            house_obj['thumb_img'] = thumb_img[0]
            house_obj['pub_time'] = pub_time[0]
            house_obj['from'] = self.name
            house_obj['img_group'] = []
            house_obj['city'] = response.extra
            house_obj['extra'] = None
            yield Item(house_obj)
if __name__ == '__main__':
    import requests

    headers = {
               "Host": "sz.zu.ke.com",
               "Referer": "https://sz.ke.com/ershoufang/",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    domain='https://sz.zu.ke.com'
    url = 'https://sz.zu.ke.com/zufang/pg0'
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
