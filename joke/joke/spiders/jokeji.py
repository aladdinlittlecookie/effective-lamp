# -*- coding: utf-8 -*-
import scrapy


class JokejiSpider(scrapy.Spider):
    name = 'jokeji'
    allowed_domains = ['jokeji.com']
    start_urls = ['http://jokeji.com/']

    def parse(self, response):
        pass
