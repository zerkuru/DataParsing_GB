import Pandas
from lxml import html
import requests
import os
import time
from pprint import pprint
from sys import argv

job_offer = argv

print (f"We wıll search for {job_offer}\n")

r_HH = requests.get('https://hh.ru/search/vacancy')
r_SJ = requests.get('https://www.superjob.ru/vakansii')


root_HH = html.fromstring(r_HH.content)
root_SJ = html.fromstring(r_SJ.content)

print "-------------------------------------\n"
print f"{root_HH}"
print "-------------------------------------\n"
print f"{root_SJ}"
print "-------------------------------------\n"



offers_HH = root.xpath("//article")
offers_SJ = root.xpath("//article")

for article in articles:
    title = article.xpath(«.//h3/a/@title»)[0]
    image = article.xpath(«.//div[@class=‘image_container']/a/img/@src")[0]
    price = article.xpath(«.//p[@class=‘price_color']/text()")[0]
    instock = article.xpath(".//p[contains(@class, 'instock')]/text()")
    print(title, image, price, instock)[0]

