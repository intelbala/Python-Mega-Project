#Database implementation using SQLLITE3
#sqllite3 comes built in with python

import sqlite3

""" 
sqllite3 
- Python library to interact with SQLLite database. SQL code can be written inside python using sqllite3
- This is not the actual SQLLite database. SQLLite database can be created as a file and hence this application can be 
    distributed to anyone without having to install sqllite. 
psycopg2

Steps for working with database
1. Connect to a database
2. Create a cursor object
3. Write a Sql query
4. Commit changes
5. Close the connection
"""
def create_table():
    conn = sqlite3.connect("lite.db")    #open database file. If it doesnt exist, this command will create the same. 
    cur = conn.cursor()                 #create a cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #Create a new table if that does not exists
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")    #open database file. If it doesnt exist, this command will create the same. 
    cur = conn.cursor()                 #create a cursor object
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")    #open database file. If it doesnt exist, this command will create the same. 
    cur = conn.cursor()                 #create a cursor object
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")    #open database file. If it doesnt exist, this command will create the same. 
    cur = conn.cursor()                 #create a cursor object
    cur.execute("DELETE FROM store WHERE item=?",(item,))  #item, - comma is required to avoid incorrect number of bindings error
    conn.commit()
    conn.close()

def update(item, quantity, price):
    er = sqlite3.Error()
    conn = sqlite3.connect("lite.db")    #open database file. If it doesnt exist, this command will create the same. 
    cur = conn.cursor()                 #create a cursor object
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    conn.commit()
    conn.close()


#insert("Wine Glass", 5, 1.99)
#delete('Wine Glass')
update('Wine Glass', 5, 4.99)
print(view())
