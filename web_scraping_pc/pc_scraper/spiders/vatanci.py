import scrapy
from ..items import VatanScraperItem


# spider class
class VatanciSpider(scrapy.Spider):

    # spider name
    name = "vatanci"

    # url
    allowed_domains = ["www.vatanbilgisayar.com"]

    # start url
    start_urls = ["https://www.vatanbilgisayar.com/notebook/?page=1"]

    # parse method
    def parse(self, response):
        # get all url from page
        product_urls = response.css("a.product-list__link::attr(href)").getall()

        # next page
        page = response.css(".pagination__item:nth-child(6) .pagination__content::attr(href)").get()

        next_page = response.urljoin(f"https://www.vatanbilgisayar.com{page}")

        # with for loop append to item field
        for url in product_urls:
            # item
            url_list = VatanScraperItem()
            url_list["urls"] = f"https://www.vatanbilgisayar.com/{url}#urun-ozellikleri"

            yield url_list

        yield scrapy.Request(next_page)