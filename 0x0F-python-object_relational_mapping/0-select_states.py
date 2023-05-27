#!/usr/bin/python3
"""Module that Get all states"""
import MySQLdb
import sys

u_name = sys.argv[1]
passw = sys.argv[2]
d_base = sys.argv[3]

db = MySQLdb.connect(host="localhost", port=3306, user=u_name, password=passw, database=d_base)

curs = db.cursor()
curs.execute("SELECT * FROM states ORDER BY states.id ASC")
res = curs.fetchall()

for i in res:
    print(i)

curs.close()
db.close()
