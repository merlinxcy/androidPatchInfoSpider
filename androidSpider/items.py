# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AndroidspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cve_id = scrapy.Field()
    patch_date = scrapy.Field()
    type = scrapy.Field()
    level = scrapy.Field()
    affect_version = scrapy.Field()


