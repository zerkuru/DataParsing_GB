from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from LBscraper import settings
from LBscraper.spiders.LB import LBSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LBSpider)
# process.crawl(SjruSpider)
    process.start()
