import scrapy
import json
from ..items import ProductSpider

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
                yield scrapy.Request(url=url["urls"], callback=self.parse_product, cb_kwargs={"url": url["urls"]})

    def parse_product(self, response, url):

        # features to item section
        features_item = ProductSpider()

        # features parsed
        features_parsed = response.css("ul.pdetail-property-list li span::text").getall()

        # assignent
        features_item["ram"] = features_parsed[11]

        features_item["processor_gen"] = features_parsed[3]

        features_item["processor_brand"] = features_parsed[1]

        features_item["ram_type"] = features_parsed[13]

        features_item["processor_boost"] = features_parsed[9]

        features_item["processor_id"] = features_parsed[7]

        if features_parsed[-1].endswith("GB"):
            features_item["disk"] = features_parsed[-1]
        else:
            features_item["disk"] = "None"

        # if nvida is available
        if "rtx" in url:
            features_item["gpu"] = url[url.index("rtx"):url.index("rtx")+7]
        else:
            features_item["gpu"] = "None"

        yield features_item
