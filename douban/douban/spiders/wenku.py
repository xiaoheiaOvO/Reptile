#-*- codeing = utf-8 -*-
#@Time : 2021/5/24 20:16
#@Author : 小黑
#@File : wenku.py
#@Software : PyCharm


import scrapy
from bs4 import BeautifulSoup
import requests

url='https://wenku.baidu.com/view/cb6c68d886c24028915f804d2b160b4e777f819d.html'
res = requests.get(url)
bs = BeautifulSoup(res.text,'html.parser')
datas = bs.find_all('div',class_='ie-fix')
#遍历
for data in datas:
    print(data.text,end='')

