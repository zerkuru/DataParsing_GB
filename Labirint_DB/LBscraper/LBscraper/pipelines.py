# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class MvscraperPipeline:
    def process_item(self, item, spider):
        return item



class MvscraperPipeline(object):
    def __init__(self):
        client = MongoClient('localhost',27017)
        self.mongobase = client.offer_280
    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        print(item['price'])
        return item
