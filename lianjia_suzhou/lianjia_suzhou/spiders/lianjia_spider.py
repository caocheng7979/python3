# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia_spider'
    allowed_domains = ['su.lianjia.com']
    start_urls = ['http://su.lianjia.com/']

    def parse(self, response):
        print('OK!')
