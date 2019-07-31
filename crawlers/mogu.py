#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base.gen_task import TaskProducer


class MoguCrawler():
    name='mogu'
    def crawl(self, url_data):
        area_pat = self.re.compile(r'(\d{1,5}\.\d)㎡') #TODO 得去掉这个
        ori_url = url_data.get('url')
        page = url_data.get('page')
        city_id = url_data.get('city_id')


        headers = {
            "Host": "api.mgzf.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "http://sz.mgzf.com/list/pg4/?searchWord=",
            "Content-Type": "application/x-www-form-urlencoded",
            "Channel": "3",
            "UUID": "ad508977-0e95-7a5c-72a7-c93e5ebfb354",
            "Content-Length": "49",
            "Origin": "http://sz.mgzf.com",
            "Connection": "keep-alive",
        }

        post_data = {
            'currentPage': page,
            'cityId': int(city_id),
            'showCount': 18,
            'searchWord': ''
        }
        domain = ori_url
        url = 'https://api.mgzf.com/room-find-web/find/list'
        resp = self.requests.post(url, headers=headers, data=post_data)
        all_data = resp.json()
        houses_data = all_data['content']['list']
        house_li = []
        for house in houses_data:
            house_obj = dict()
            house_obj['title'] = house['title']
            house_obj['house_url'] = domain + '/room/{}.shtml'.format(house['roomId'])
            house_obj['district'] = house['title'].split('-')[0]
            house_obj['loc'] = house['title']
            house_obj['struct'] = house['subTitle']
            house_obj['area'] = area_pat.findall(house['subTitle'])[0]
            house_obj['rent'] = house['showPrice']
            house_obj['attr'] = house['detailDesc'] + house['location']
            house_obj['community_name'] = house['title'].split('-')[-1]
            house_obj['thumb_img'] = house['pictureUrl']
            house_obj['pub_time'] = ''
            house_obj['img_group'] = []
            house_obj['extra'] = None
            house_li.append(house_obj)
        return house_li

if __name__ == '__main__':

    import requests,re
    area_pat = re.compile(r'(\d{1,5}\.\d)㎡')

    headers = {
        "Host": "api.mgzf.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "http://sz.mgzf.com/list/pg4/?searchWord=",
        "Content-Type": "application/x-www-form-urlencoded",
        "Channel": "3",
        "UUID": "ad508977-0e95-7a5c-72a7-c93e5ebfb354",
        "Content-Length": "49",
        "Origin": "http://sz.mgzf.com",
        "Connection": "keep-alive",
    }

    post_data={
        'currentPage': 3,
        'cityId': 340,
        'showCount': 18,
        'searchWord': ''
    }
    domain='http://sz.mgzf.com'
    url = 'https://api.mgzf.com/room-find-web/find/list'
    resp = requests.post(url,headers=headers,data=post_data)
    all_data = resp.json()
    houses_data=all_data['content']['list']
    for house in houses_data:
        house_obj = dict()
        house_obj['title'] = house['title']
        house_obj['house_url'] = domain+'/room/{}.shtml'.format(house['roomId'])
        house_obj['district'] = house['title'].split('-')[0]
        house_obj['loc'] = house['title']
        house_obj['struct'] = house['subTitle']
        house_obj['area'] = area_pat.findall(house['subTitle'])[0]
        house_obj['rent'] = house['showPrice']
        house_obj['attr'] = house['detailDesc']+house['location']
        house_obj['community_name'] = house['title'].split('-')[-1]
        house_obj['thumb_img'] = house['pictureUrl']
        house_obj['pub_time'] = ''
        house_obj['img_group'] = []
        house_obj['extra'] = None
        print(house_obj)
