import scrapy
import json


class ProductspiderSpider(scrapy.Spider):
    # name
    name = "productspider"

    # domain
    allowed_domains = ["www.vatanbilgisayar.com"]

    start_urls = ["https://www.vatanbilgisayar.com/notebook/?page=1"]

    def parse(self, response):
        # url
        with open("/home/charon5/web_scraping/web_scraping/vatan_scraper/vatan_scraper/products_urls.json", "r", encoding="utf-8") as file:
            for url in json.loads(file.read()):
                yield scrapy.Request(url=url["urls"], callback=self.parse_product)

    def parse_product(self, response):
        yield {"m": response.css("ul.pdetail-property-list li span::text").getall()}
