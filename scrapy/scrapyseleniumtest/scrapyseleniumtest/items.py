# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field


class ScrapyseleniumtestItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProductItem(Item):
    collection = 'product'
    image = Field()
    price = Field()
    deal = Field()
    title = Field()
    shop = Field()
    location = Field()
