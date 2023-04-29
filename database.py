
import sqlite3
import json


def makebase():
    connector_db = sqlite3.connect('news.db')
    cur = connector_db.cursor()

    #tables making
    

    cur.execute("""CREATE TABLE IF NOT EXISTS news(
      newsid INT PRIMARY KEY,
      title TEXT,
      href TEXT,
      source TEXT,
      datestring TEXT);
      """)
    connector_db.commit()


def inputnews_json(json_string):
    connector_db = sqlite3.connect('db.sqlite')
    cursor = connector_db.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS news(
      newsid INT PRIMARY KEY,
      title TEXT,
      href TEXT,
      source TEXT,
      datestring TEXT);
      """)
    
    columns = ['title','href','source', 'datestring']
    for row in json_string:
        keys= tuple(row[c] for c in columns)
        cursor.execute('insert into news values(?,?,?)',keys)
        print(f'{row["title"]} data inserted Succefully')
        
    connector_db.commit()


connection.commit()
connection.close()
 


