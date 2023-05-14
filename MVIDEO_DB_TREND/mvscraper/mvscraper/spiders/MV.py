import scrapy

class MvSpider(scrapy.Spider):
    name = "MV"
    allowed_domains = ["www.mvideo.ru"]
    start_urls = ["http://www.mvideo.ru/"]

    def parse(self, response):
        pass
from scrapy.http import HtmlResponse
from mvscraper.items import MvscraperItem

class MvSpider(scrapy.Spider):
    name = "MV"
    allowed_domains = ["www.mvideo.ru"]
    start_urls = ["https://www.mvideo.ru/promo/likvidaciya-tovarov-skidki-do-50-mark203346425?from=pk_main_menu"]

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.HH-Pager-ControlsNext::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)
        offer = response.css(
            'div.vacancy-serp div.vacancy-serp-item div.vacancy-serpitem__row_header a.bloko-link::attr(href)'
            ).extract()
        for link in offer:
            yield response.follow(link, callback=self.offer_parse)
    
    def offer_parse(self, response: HtmlResponse):
        name = response.css('div.vacancy-title h1.header::text').extract_first()
        price = response.css('div.vacancy-title p.vacancysalary::text').extract()
        # print(name, price)
        yield MvscraperItem(name=name,price=price)

