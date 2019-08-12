#!/usr/bin/env python
# -*- coding:utf-8 -*-
city_map={}
import requests
headers={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
# "Cookie":"lianjia_uuid=be4869b5-bafe-4267-ad50-53d875b8b8c6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c1de09f983b9-0fcc1e4938127c-9333061-1296000-16c1de09f991e4%22%2C%22%24device_id%22%3A%2216c1de09f983b9-0fcc1e4938127c-9333061-1296000-16c1de09f991e4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDxD930YhFb0nsg60Zpc77I00000AR-Q7C00000ILVnTm.THvkVQOZ0A3qmh7GuZR0T1dBnyD3m1f4P10snjDvnHDv0ZRqfH-ArHD3PjT3rRRdnWmkrjDvnDmYwj6YnDDsfRmLnHR%22%2C%22%24latest_referrer_host%22%3A%22sp0.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wyshenzhen%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; lianjia_ssid=7963efe3-0ce7-40da-a213-229b828c018b; select_city=310000; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYjZhZWZkNTVhNWM2YjM0ZGI1ZWY5YzU0YTM2MDg2NGRiMTNmMjRjNzEwODMzNmZiNmVjMGRkNDBmZDEyOTIxYmEzZTFmY2Q3NzUxYjEwMDZiNTdjYjExZGY4MTQ1MjliMDI5MjJlY2M4M2YzMjRhMWMzYTllMGJhYWVhNTdkMGVjYTVjZDBlNjFjY2IwZGEwODkxZTM4ZDc3MjU0Yzc4OGE3NDQ0OTJhZTZmNTA0NGI4MDFiMWMzZjFmMTg1NjNiZDY5ZWFkNmExYWU3YjgzZDUzMzE4NTU1NjA3MGY4N2NkMWFlYmU1MGU2NjkzYzcwMjY3MWI2MzdjMWEwYTJmZDQwMzFlMzYwNTI5MmFjOTEzOTE1ZWQ5YjcxNjk4YTZmNDc5OGZiYWYxNjQ3Y2NiZDgzMmEyNGI4N2E1NjhjMDMwM2U1MzY4MjJjMWZjMDJlZjBlM2E4NjEzZTVlNTc2ZVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIwYjYyNWE4ZlwifSIsInIiOiJodHRwczovL3d3dy5rZS5jb20vY2l0eS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==",
"Host":"www.ke.com",
"Pragma":"no-cache",
"Referer":"https://sh.ke.com/",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
}
# html=requests.get('https://www.ke.com/city/',headers=headers).text
# from lxml import etree
# dom=etree.HTML(html)
# cities=['成都','东莞','合肥','北京','重庆','泉州','贵阳','长沙','杭州','宁波','厦门','武汉','苏州','西安','广州','郑州','济南','上海','福州','南京','天津','深圳']
# cities_dom=dom.xpath('//li[@class="CLICKDATA"]/a')
# c_data=[]
# for citydom in cities_dom:
#     url=citydom.xpath('./@href')
#     c_name=citydom.xpath('./text()')
#     if c_name[0] in cities:
#         citydic = dict()
#         citydic['cname'] = c_name[0]
#         citydic['curl'] = 'https:' + url[0]
#         c_data.append(citydic)
# print(c_data)
li=[{'cname': '北京', 'curl': 'https://bj.ke.com'}, {'cname': '上海', 'curl': 'https://sh.ke.com'}, {'cname': '广州', 'curl': 'https://gz.ke.com'}, {'cname': '深圳', 'curl': 'https://sz.ke.com'}, {'cname': '成都', 'curl': 'https://cd.ke.com'}, {'cname': '合肥', 'curl': 'https://hf.ke.com'}, {'cname': '北京', 'curl': 'https://bj.ke.com'}, {'cname': '重庆', 'curl': 'https://cq.ke.com'}, {'cname': '福州', 'curl': 'https://fz.ke.com'}, {'cname': '厦门', 'curl': 'https://xm.ke.com'}, {'cname': '泉州', 'curl': 'https://quanzhou.ke.com'}, {'cname': '广州', 'curl': 'https://gz.ke.com'}, {'cname': '深圳', 'curl': 'https://sz.ke.com'}, {'cname': '东莞', 'curl': 'https://dg.ke.com'}, {'cname': '贵阳', 'curl': 'https://gy.ke.com'}, {'cname': '郑州', 'curl': 'https://zz.ke.com'}, {'cname': '武汉', 'curl': 'https://wh.ke.com'}, {'cname': '长沙', 'curl': 'https://cs.ke.com'}, {'cname': '南京', 'curl': 'https://nj.ke.com'}, {'cname': '苏州', 'curl': 'https://su.ke.com'}, {'cname': '上海', 'curl': 'https://sh.ke.com'}, {'cname': '济南', 'curl': 'https://jn.ke.com'}, {'cname': '成都', 'curl': 'https://cd.ke.com'}, {'cname': '西安', 'curl': 'https://xa.ke.com'}, {'cname': '天津', 'curl': 'https://tj.ke.com'}, {'cname': '杭州', 'curl': 'https://hz.ke.com'}, {'cname': '宁波', 'curl': 'https://nb.ke.com'}]
temp = dict()
for i in li:
    temp[i['curl']] = i['cname']
print(temp)
