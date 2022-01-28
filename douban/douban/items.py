# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#定义一个类DoubanItem，它继承自scrapy.Item
class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 定义书名的数据属性
    title = scrapy.Field()
    # 定义出版信息的数据属性
    publish = scrapy.Field()
    # 定义评分的数据属性
    score = scrapy.Field()
    pass


#当当网
class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    publisher = scrapy.Field()
    price = scrapy.Field()

    pass


#职友集
class JobuiItem(scrapy.Item):
#定义了一个继承自scrapy.Item的JobuiItem类
    company = scrapy.Field()
    #定义公司名称的数据属性
    position = scrapy.Field()
    #定义职位名称的数据属性
    address = scrapy.Field()
    #定义工作地点的数据属性
    detail = scrapy.Field()
    #定义招聘要求的数据属性