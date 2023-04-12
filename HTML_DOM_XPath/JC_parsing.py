import Pandas
from lxml import html
import json
import requests
import os
import time
from pprint import pprint
from sys import argv
#не вижу смысла парсить super job через html, имена классов генерируются скриптом. У них есть API как и у HH

def parseJC():   
    print('Enter your choices of job offers:')
    job_offer_list = input().strip().split(" ")

    print("Enter the page link HH")
    linkpage = input().strip()

    print (f"We wıll search for {job_offer_list}\n")

    r_HH = requests.get(linkpage)
    root_HH = html.fromstring(r_HH.content)
    offers_HH = root_HH.xpath(".//dıv[contains(@class, 'vacancy-serp-item-body__main-info')]")

    hh_offers = []

    for offer in offers_HH:
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
        hh_offers.append(new_offer)


    json_result = json.dumps(hh_offers)

    with open("hh.json", "w") as outfile:
        outfile.write(json_result)