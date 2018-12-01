# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# import scrapy


import scrapy


class MztuItem(scrapy.Item):
    #目录
    title = scrapy.Field()
    #图片地址
    imge_url = scrapy.Field()
    #请求头
    Referer = scrapy.Field()

    image_Path = scrapy.Field()
    #图片名称
   # nickname = scrapy.Field()