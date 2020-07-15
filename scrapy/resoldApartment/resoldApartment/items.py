# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ResoldApartmentItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    zoning = Field()  # 划分区域
    area = Field()  # 面积
    floor = Field()  # 楼层
    construction_time = Field() # 建造时间
    intro = Field() # 简介
    price = Field() # 价格



