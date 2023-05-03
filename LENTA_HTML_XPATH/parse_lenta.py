
import json
from lxml import html

def parse_for_news(request_result):

    json_string = ''

    with open('lenta_today.json', 'w', encoding='utf-8') as output_file:

        root_lenta = html.fromstring(request_result.content)
        my_arefs  = root_lenta.xpath(".//a[contains(@class, 'card_mini _topnews')]")

        newslist = []
        newsset = {}

        for i in my_arefs:
            
            title = i.xpath(".//span/a[@class='card-mini__title']/text()")[0]

            date_news = i.xpath(".//time/a[@class='card-mini__date']/text()")[0]

            href_news = i.xpath(".href()")[0]

            newsset['title'] = title
            newsset['datestring'] = date_news
            newsset['href'] = href_news
            newsset['source'] = 'lenta.ru'
            newslist.append(newsset)
        
        json_string = json.dumps(newslist)
        output_file.write(json_string)
    
    return json_string