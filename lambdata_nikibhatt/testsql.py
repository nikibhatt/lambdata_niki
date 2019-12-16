
import sqlite3
import os

conn = sqlite3.connect('toy_data.db')

# query = 'CREATE TABLE toy (name varchar(30), size int);'
# curs = conn.cursor()
# curs.execute(query)
# curs.close()
# conn.commit()


# insert_query = 'INSERT INTO toy (name, size) VALUES ("awesome", 27);'

curs = conn.cursor()

curs.execute('SELECT * from toy;')

print(curs.fetchall())

curs.close()
conn.commit()
