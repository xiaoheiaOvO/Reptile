#-*- codeing = utf-8 -*-
#@Time : 2021/3/29 16:17
#@Author : 小黑
#@File : top60_2018.py
#@Software : PyCharm

import scrapy
from bs4 import BeautifulSoup

from ..items import DangdangItem

class DangDangSpider(scrapy.Spider):
    name = 'dangdang'

    allowed_domains = ['http://bang.dangdang.com']

    start_urls = []
    for i in range(1,4):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-'+str(i)
        start_urls.append(url)

    def parse(self,response):
        bs = BeautifulSoup(response.text,'html.parser')
        datas = bs.find('ul',class_='bang_list clearfix bang_list_mode').find_all('li')
        for data in datas:
            item = DangdangItem()
            item['name'] = data.find('div',class_='name').text
            item['publisher'] = data.find_all('div',class_='publisher_info')[0].text
            item['price'] = data.find('span',class_='price_n').text

            yield item

