import LENTA_HTML_XPATH.parse_lenta as parse_lenta
import LENTA_HTML_XPATH.database as database
import requests
import json
from lxml import html


print ("Welcome to news parsing app")

#

def main():
    
    url = 'https://lenta.ru//'
  
    r = requests.get(url)

    json_string = parse_lenta.parse_for_news(r)

    database.make_base()

    database.inputnews_json(json_string)

    print("Thank you for using the app!")

 
# Запуск кода
if __name__ == '__main__':
    main()

