import scrapy


class TryalSpider(scrapy.Spider):
    name = "tryal"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
