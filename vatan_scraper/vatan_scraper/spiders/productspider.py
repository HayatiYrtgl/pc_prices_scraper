import scrapy
import json

class ProductspiderSpider(scrapy.Spider):
    # name
    name = "productspider"

    # domain
    allowed_domains = ["www.vatanbilgisayar.com"]

    # url
    start_urls = ["https://"]

    def parse(self, response):
        pass
