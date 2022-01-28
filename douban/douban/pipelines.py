# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import openpyxl

class DoubanPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['公司', '职位', '地址', '招聘信息'])


    def process_item(self, item, spider):
        line = [item['company'], item['position'], item['address'], item['detail']]
        # 把公司名称、职位名称、工作地点和招聘要求都写成列表的形式，赋值给line
        self.ws.append(line)
        return item

    def close_spdier(self,spider):
        self.wb.save('douban.xlsx')
        self.wb.close()
