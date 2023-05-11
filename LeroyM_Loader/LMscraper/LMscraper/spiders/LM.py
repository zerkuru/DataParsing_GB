import scrapy

from scrapy.http import HtmlResponse
from LMscraper.items import LMscraperItem

class LMSpider(scrapy.Spider):
    name = "LM"
    allowed_domains =  ["www.labirint.ru"]
    start_urls = ["https://www.labirint.ru/"]

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
        author = response.css('div.vacancy-title p.vacancysalary::text').extract()
        discount_price = response.css('div.vacancy-title p.vacancysalary::text').extract()
        rating = response.css('div.vacancy-title p.vacancysalary::text').extract()
        # print(name, price)
        yield MvscraperItem(name=name,price=price, author=author, discount_price=discount_price, rating=rating)



