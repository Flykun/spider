# -*- coding: utf-8 -*-
import scrapy
from ..items import TravelItem


class SanyaSpider(scrapy.Spider):
    name = 'Sanya'
    allowed_domains = ['https://qnee9.package.qunar.com/user/detail.jsp?abt=a&id=2801153006&filterDate=2020-06-13%2C2020-06-13&dep=JEEk#tf=%E9%83%91%E5%B7%9E_%E4%B8%89%E4%BA%9A_149&isAds=1']
    start_urls = ['https://dujia.qunar.com/pq/list_%E4%B9%9D%E5%AF%A8%E6%B2%9F?tm=4lou_nav_gn_origin']

    def parse(self, response):
        item = TravelItem()
        item['title'] = response.xpath('//div[@class="summary"]/h1/text()').extract()[1]
        item['discounts'] = ','.join(
            response.xpath('//div[@class="features"]/span/span/text()').extract())
        item['price'] = response.xpath('//var[@id="js-min-price"]/text()').extract_first()
        yield item
