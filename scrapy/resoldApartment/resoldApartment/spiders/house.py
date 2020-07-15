# -*- coding: utf-8 -*-

from scrapy import Spider
from ..items import ResoldApartmentItem


class HouseSpider(Spider):
    name = 'house'
    allowed_domains = ['zhengzhou.anjuke.com/sale']
    start_urls = ['https://zhengzhou.anjuke.com/sale/']

    def parse(self, response):
        results = response.xpath('//*[@id="houselist-mod-new"]/li')
        for result in results:
            item = ResoldApartmentItem()
            item['title'] = result.xpath(
                'div[@class="house-details"]/div[@class="house-title"]/a/text('
                ')').extract_first().strip()
            item['zoning'] = result.xpath(
                'div[@class="house-details"]/div[@class="details-item"]/span[1]/text('
                ')').extract_first()
            item['area'] = result.xpath(
                'div[@class="house-details"]/div[@class="details-item"]/span[2]/text('
                ')').extract_first()  # 面积
            item['floor'] = result.xpath(
                'div[@class="house-details"]/div[@class="details-item"]/span[3]/text('
                ')').extract_first()  # 楼层
            item['construction_time'] = result.xpath(
                'div[@class="house-details"]/div[@class="details-item"]/span[4]/text('
                ')').extract_first()
            item['intro'] = result.xpath(
                'div[@class="house-details"]/div[@class="details-item"]/span['
                '@class="comm-address"]/text()').extract_first().rstrip()  # 简介
            item['price'] = result.xpath(
                'div[@class="pro-price"]/span/strong/text()').extract_first()
            yield item
