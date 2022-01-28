#-*- codeing = utf-8 -*-
#@Time : 2021/3/29 15:20
#@Author : 小黑
#@File : top250.py
#@Software : PyCharm

import scrapy
from bs4 import BeautifulSoup

#固定用法
from ..items import DoubanItem

#定义爬虫类，继承自scrapy.Spider类
class DoubanSpider(scrapy.Spider):
    #定义爬虫名字，是爬虫唯一的标识
    name = 'douban'
    #定义允许爬虫爬取的网址域名，不在域名中的则过滤
    allowed_domains = ['https://book.douban.com']
    #起始网址
    start_urls = []
    for x in range(3):
        url = 'https://book.douban.com/top250?start=0' + str(x*25)
        start_urls.append(url)

    #默认解析response方法
    def parse(self, response):
        bs = BeautifulSoup(response.text,'html.parser')
        datas = bs.find_all('tr',class_='item')
        #遍历
        for data in datas:
            item = DoubanItem()
            # 提取书名
            item['title'] = data.find_all('a')[1]['title']
            item['publish'] = data.find('p',class_='pl').text
            item['score'] = data.find('span',class_='rating_nums').text
            #print(item['title'])

            #把获得的item传递给引擎
            #它有点类似return，不过它和return不同的点在于，它不会结束函数，且能多次返回信息。
            yield item