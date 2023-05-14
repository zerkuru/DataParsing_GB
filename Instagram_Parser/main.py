import InstagramParser.parse_inst as parse_inst
import InstagramParser.get_list as get_list
import InstagramParser.database as database
import requests
import json
from lxml import html


print ("Welcome to instagram parsing app")

#

def main():
    
    urls = get_list.geturls()
    database.make_base()
  
    for url in urls:
        r = requests.get(url)
        json_string_subscribers = parse_inst.parse_for_subscribers(r)
        json_string_subscribed_to = parse_inst.parse_for_subscribed_to(r)

    database.inputnew_json(json_string_subscribers)

    database.inputnew_json(json_string_subscribed_to)

    print ("To find subscribers or subscribed to, input the user name, choose option, get result. \n To stop the app, print q, to start - print s")

    i = 1
    while i:
        comandnew = input("Input your comand - s - start, q - quit")
        if comandnew == "q":
            break
        comandnew = input("Enter the user name: ")
        userid = database.finduser(comandnew)
        comandnew = input("Enter subscriber or following (s or f):")
        response_result = ""
        if comandnew == "s":
            respoonse_result = database.getsubscribers(userid)
        else:
            response_result = database.getfollowed(userid)
        print (response_result)

   print ("Thanks for using the app")





    print("Thank you for using the app!")

 
# Запуск кода
if __name__ == '__main__':
    main()

