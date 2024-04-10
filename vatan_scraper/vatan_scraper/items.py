# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VatanScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urls = scrapy.Field()


class ProductSpider(scrapy.Item):
    ram = scrapy.Field()
    gpu = scrapy.Field()
    disk = scrapy.Field()
    processor_gen = scrapy.Field()
    processor_brand = scrapy.Field()
    ram_type = scrapy.Field()
    processor_boost = scrapy.Field()
    processor_id = scrapy.Field()