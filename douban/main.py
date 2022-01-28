#-*- codeing = utf-8 -*-
#@Time : 2021/3/29 16:04
#@Author : 小黑
#@File : main.py
#@Software : PyCharm

#导入cmdline模块，可以实现控制终端命令行
from scrapy import cmdline

#用execute()方法，输入运行scrapy指令
def douban_run():
    cmdline.execute(['scrapy','crawl','douban'])

def dangdang_run():
    cmdline.execute(['scrapy','crawl','dangdang'])

def jobui_run():
    cmdline.execute(['scrapy','crawl','jobs'])

def wenku_run():
    cmdline.execute(['scrapy','crawl','wenku'])

if __name__ == '__main__':
    #dangdang_run()
    #douban_run()
    #jobui_run()
    wenku_run()