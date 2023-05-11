import requests
from bs4 import BeautifulSoup as bs
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="sa",
  password="sa"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE job_offer_db")
