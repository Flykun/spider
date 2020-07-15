# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SaleSpider(CrawlSpider):
    name = 'sale'
    allowed_domains = ['zhengzhou.anjuke.com/sale']
    start_urls = ['http://zhengzhou.anjuke.com/sale/']
    """
    https://zhengzhou.anjuke.com/prop/view/A5129491963?from=filter&spread=commsearch_p&uniqid=pc5f0ec768a1d6d9.42853327&position=2&kwtype=filter&now_time=1594804072
    https://zhengzhou.anjuke.com/prop/view/A5096315780?from=filter&spread=commsearch_p&uniqid=pc5f0ec768a1d3f3.33794278&position=1&kwtype=filter&now_time=1594804072
    """

    rules = (
        Rule(LinkExtractor(allow=r'Items/', restrict_xpaths='//*[@id="houselist-mod-new"]/li[1]/div[2]/div[1]/a'),callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
