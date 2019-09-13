# -*- coding: utf-8 -*-
"""sprint challenge 9/13/19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1liPpPdrE-J0EPDUUJzwko36MM-g16VxA
"""

import sqlite3
from sqlite3 import Error

def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close() 

if __name__ == '__main__':
    create_connection()

conn = sqlite3.connect('demo_data.db')
conn

curs = conn.cursor()
curs

query = 'CREATE TABLE demo (s varchar(30), x int, y int);'
query

curs.execute(query)

curs.close()
conn.commit()

curs2 = conn.cursor()
curs2.execute('SELECT * FROM demo;').fetchall()

insert_query = 'INSERT INTO demo (s, x, y) VALUES ("g", 3, 9);'
curs2.execute(insert_query)
curs2.execute('SELECT * FROM demo;').fetchall()

curs2.close()
conn.commit()

curs3 = conn.cursor()
insert_query2 = 'INSERT INTO demo (s, x, y) VALUES ("v", 5, 7);'
insert_query3 = 'INSERT INTO demo (s, x, y) VALUES ("f", 8, 7);'
curs3.execute(insert_query2)
curs3.execute(insert_query3)
curs3.execute('SELECT * FROM demo;').fetchall()

curs3.close()
conn.commit()

curs4 = conn.cursor()
number_of_rows = print ("Number of rows:", len(curs4.execute('SELECT * FROM demo').fetchall()))

curs4.close()
conn.commit()