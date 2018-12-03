# -*- coding: utf-8 -*-
import scrapy
from ..items import JokeItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Jokeji1Spider(CrawlSpider):
    name = 'jokeji1'
    allowed_domains = ['jokeji.cn']
    start_urls = ['http://www.jokeji.cn/jokehtml/xy/2018112823415329.htm']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.jokeji.cn/JokeHtml'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'/jokehtml/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):

        title = response.xpath("//div[@class='left_up']/h1/text()[2]").extract_first()
        cons = response.xpath("//ul/span[@id='text110']/p")
        b = [str(a.xpath('string(.)').extract_first()) for a in cons]
        con= ''.join(b)
        joke_item = JokeItem()
        joke_item["title"] = title
        joke_item["con"] = con
        yield joke_item
        # print(title,con)
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
