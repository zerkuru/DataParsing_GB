
import sqlite3
import json


def makebase():
    connector_db = sqlite3.connect('inst.db')
    cur = connector_db.cursor()

    #tables making
    

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
      userid INT PRIMARY KEY,
      name TEXT,
      href TEXT,
      instid TEXT);
      """)
    connector_db.commit()
    cur.execute("""CREATE TABLE IF NOT EXISTS subscribers(
      connectionid INT PRIMARY KEY,
      userid INT FOREIGN KEY users.userid,
      subscriberid INT FOREIGN KEY users.userid);
      """)
    connector_db.commit()
    connector_db.close()


def inputnew_json(json_string):
    connector_db = sqlite3.connect('db.sqlite')
    cursor = connector_db.cursor()
    
    columns = ['name','href','instid']
    for row in json_string:
        keys= tuple(row[c] for c in columns)
        cursor.execute('insert into users values(?,?,?)',keys)
        print(f'{row["name"]} data inserted Succefully')
        

    connector_db.commit()
    connector_db.close()


def finduser (username):
    connector_db = sqlite3.connect('db.sqlite')
    cursor = connector_db.cursor()
    
    userid = cursor.execute("""SELECT * FROM users where name = name);
      """)
    
    connector_db.close()
    return userid 

def getsubscribers(userid):
    connector_db = sqlite3.connect('db.sqlite')
    cursor = connector_db.cursor()
    
    sublist = cursor.execute("""SELECT name FROM users where userid in (SELECT subscriberid FROM subscribers where userid = userid);
      """)
    
    connector_db.close()
    return sublist 


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
    connector_db.close()

def getfollowed(userid):
    connector_db = sqlite3.connect('db.sqlite')
    cursor = connector_db.cursor()
    
    sublist = cursor.execute("""SELECT name FROM users where userid in (SELECT userid FROM subscribers where subscriberid = userid);
      """)
    
    connector_db.close()
    return sublist 
     

 


