from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from mvscraper import settings
from mvscraper.spiders.mv import MvSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(MvSpider)
# process.crawl(SjruSpider)
    process.start()
