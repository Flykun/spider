# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ChinaLoader, NewsItem


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles']

    rules = (
        Rule(LinkExtractor(
            allow=r'article/.*.html',
            restrict_xpaths='//div[@id="rank-defList"]'
        ), callback='parse_item', follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='//div[@class="pages"]/ul/a[contains(., "下一页")]'
        ))
    )

    def parse_item(self, response):
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath('title', '//h1[@id="chan_newsTitle"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('text', '//div[@id="chan_newsDetail"]//text()')
        loader.add_xpath('datetime', '//span[@class="time"]/text()',
                         re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source', '//span[@class="source"]/text()', re='来源：(.*)')
        loader.add_value('website', '中华网')
        yield loader.load_item()
