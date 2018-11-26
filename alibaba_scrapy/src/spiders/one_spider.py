# -*- coding: utf-8 -*-
import scrapy


class OneSpiderSpider(scrapy.Spider):
    name = 'one_spider'
    allowed_domains = ['aliexpress.com']
    start_urls = ['https://sale.aliexpress.com/__pc/inspiration_tech_pc.htm?spm=2114.11010108.01004.1.650c649bbSVKYA&pid=32661554901']

    def parse(self, response):
        prices = response.css("a").extract()
        print(prices)
