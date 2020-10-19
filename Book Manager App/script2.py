""" 
Database implementation using POSTGRE SQL and Psycopg2
postgre sql and psycopg2 need to be installed manually
installing postgresql:
https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart
sudo apt-get install python-psycopg2
"""

import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='book_data' user='postgres' password='postgres' host='localhost' port='5432'")    #open database file. If it doesnt exist, this command will create the same. 
    cur = conn.cursor()                 #create a cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #Create a new table if that does not exists
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='book_data' user='postgres' password='postgres' host='localhost' port='5432'")    #open database file. If it doesnt exist, this command will create the same. 
    cur = conn.cursor()                 #create a cursor object
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')"%(item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='book_data' user='postgres' password='postgres' host='localhost' port='5432'")    #open database file. If it doesnt exist, this command will create the same. 
    cur = conn.cursor()                 #create a cursor object
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='book_data' user='postgres' password='postgres' host='localhost' port='5432'")    #open database file. If it doesnt exist, this command will create the same. 
    cur = conn.cursor()                 #create a cursor object
    cur.execute("DELETE FROM store WHERE item=%s",(item,))  #item, - comma is required to avoid incorrect number of bindings error
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = psycopg2.connect("dbname='book_data' user='postgres' password='postgres' host='localhost' port='5432'")    #open database file. If it doesnt exist, this command will create the same. 
    cur = conn.cursor()                 #create a cursor object
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    conn.commit()
    conn.close()

#create_table()
#insert("Wine Glass", 5, 1.99)
#insert("Orange", 1, 0.99)
#insert("Milk", 5, 3.99)
# delete("Orange")
# insert("Orange", 1, 10.99)
update("Orange", 1, 0.99)

print(view())

