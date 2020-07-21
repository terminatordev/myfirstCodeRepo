import sqlite3

connection=sqlite3.connect('mydata.db')
cursor=connection.cursor()

create_table_query="CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name text,password text)"
cursor.execute(create_table_query)

create_items_table_query="CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY,name text,price real)"
cursor.execute(create_items_table_query)

insert_items="INSERT INTO items VALUES(NULL,?,?)"
# cursor.execute(insert_items,('mybike',198734.12))

connection.commit()

query="SELECT * from items"

result=cursor.execute(query)

for row in result:
    print(row)
connection.close()
