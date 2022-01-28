#-*- codeing = utf-8 -*-
#@Time : 2021/3/30 21:52
#@Author : 小黑
#@File : jobui_jobs.py
#@Software : PyCharm

import scrapy
from bs4 import BeautifulSoup
from ..items import JobuiItem

class JobuiSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['https://www.jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    def parse(self, response):
        bs = BeautifulSoup(response.text,'html.parser')
        ul_list = bs.find_all('ul', class_='textList flsty cfix')
        for ul in ul_list:
            a_list = ul.find_all('a')
            for a in a_list:
                company_id = a['href']
                url = 'https://www.jobui.com{id}jobs'
                real_url = url.format(id=company_id)
                # 用yield语句把构造好的request对象传递给引擎。
                # 用scrapy.Request构造request对象。
                # callback参数设置调用parsejob方法。
                #实现从一个网站爬取下一个网站的效果
                yield scrapy.Request(real_url,callback=self.parse_job)

    def parse_job(self,response):
        bs = BeautifulSoup(response.text,'html.parser')
        company = bs.find('a',class_='company-banner-name').text
        datas = bs.find_all('div',class_='c-job-list')
        for data in datas:
            item = JobuiItem()
            # 实例化JobuiItem这个类
            item['company'] = company
            # 把公司名称放回JobuiItem类的company属性里
            item['position'] = data.find('h3').text
            # 提取出职位名称，并把这个数据放回JobuiItem类的position属性里
            item['address'] = data.find_all('span')[0].text
            # 提取出工作地点，并把这个数据放回JobuiItem类的address属性里
            item['detail'] = data.find_all('span')[1].text
            # 提取出招聘要求，并把这个数据放回JobuiItem类的detail属性里
            yield item
            # 用yield语句把item传递给引擎