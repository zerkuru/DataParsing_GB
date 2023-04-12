import Pandas
from lxml import html
import json
import requests
import os
import time
from pprint import pprint
from sys import argv
#не вижу смысла парсить super job через html, имена классов генерируются скриптом. У них есть API как и у HH

print('Enter your choices of job offers:')
job_offer_list = input().strip().split(" ")

print("Enter the page link HH")
linkpage = input().strip()

print (f"We wıll search for {job_offer_list}\n")

r_jc = requests.get(linkpage)
root_jc = html.fromstring(r_jc.content)
offers_jc = root_jc.xpath(".//dıv[contains(@class, 'vacancy-serp-item-body__main-info')]")

jc_offers = []

for offer in offers_jc:
    title = offer.xpath(".//div/h3/span/a[@class='serp-item__title']/text()")[0]
    salaryline = offer.xpath(".//span[@data-qa='vacancy-serp__vacancy-compensation']/text()")[0]
    salarylinelist = salaryline.split(" ")
    salaryintlist = []
    for i in salarylinelist:
        if (int(i)>0):
            salaryintlist.append(int(i))
    salaryintlist.sort()
    if (len(salaryintlist)>1):
        maxsalary = salaryintlist[-1]
        minsalary = salaryintlist[0]
    elif (len(salaryintlist = 1)):
        minsalary = 0
        maxsalary = salaryintlist[0]
    else:
        minsalary = 0
        maxsalary = 0

    link = offer.xpath(".//div/h3/span/a[@class='serp-item__title']/@href")[0]
    sourcesite = linkpage
    new_offer = {'title': title, 'min_salary': minsalary, 'maxsalary': maxsalary, 'link': link, 'source': sourcesite}
    jc_offers.append(new_offer)



json_result = json.dumps(jc_offers)

with open("jc.json", "w") as outfile:
    outfile.write(json_result)





