# -*- coding: utf-8 -*-
import scrapy
from ..items import MztuItem

class Mzitu2Spider(scrapy.Spider):
    name = 'mzitu2'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/xinggan/page/{}/'.format(str(x)) for x in range(131)]

    def parse(self, response):
        #解析出链接
        set_li = response.xpath("//div[@class='postlist']/ul/li")
        for ecth in set_li:
            ed = ecth.xpath('./a/@href').extract()
            #进行二次分类解析
            yield scrapy.Request(ed[0],callback=self.parse_item)


    def parse_item(self,response):
        itme = MztuItem()
        # 获取页数链接进行访问
        offset = int(response.xpath('//div[@class="pagenavi"]/a/span/text()')[4].extract())
        #生成链接访问
        #遍历链接访问
        for i in [response.url+"/{}".format(str(x))  for x in range(1,offset+1)]:
            # print(response.url,222222222222222)
            print(i,11111111111111111111)
            itme['Referer']=i
            #将meta传入链接
            yield scrapy.Request(itme['Referer'],meta={'meta_1':itme}, callback=self.parse_ponse)
        # for i in url:

    def parse_ponse(self,response):
        #获取itme资源
        itme = response.meta['meta_1']
        #获取图片地址
        imgs = response.xpath('//div[@class="main-image"]/p/a/img/@src')[0].extract()
        #获取图片目录
        title = response.xpath('//div[@class="main-image"]/p/a/img/@alt')[0].extract()
        # print(imgs,1111111111)
        itme["title"]= title
        itme["imge_url"]= imgs
        #itme["nickname"] = itme["Referer"][itme["Referer"].rfind("/"):]+itme["imge_url"][itme["imge_url"].rfind('/')+1:itme["imge_url"].rfind('.')]
        #itme["nickname"] = itme["imge_url"][itme["imge_url"].rfind('/')+1:itme["imge_url"].rfind('.')]
        yield itme
