# -*- coding: utf-8 -*-

from scrapy import Spider, Request


class WeibocnSpider(Spider):
    name = 'weibocn'
    allowed_domains = ['m.weibo.cn']
    user_url = ''
    follow_url = ''
    fan_url = ''
    weibo_url = ''
    start_users = []

    def start_requests(self):
        for uid in self.start_users:
            yield Request(self.user_url.format(uid=uid), callback=self.parse_user)


    def parse_user(self, response):
        self.logger.debug(response)
