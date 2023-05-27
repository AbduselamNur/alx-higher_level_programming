#!/usr/bin/python3
"""Module that Get all states"""
import MySQLdb


db = MySQLdb.connect(host="localhost", port=3306, user="root", password="root", database="hbtn_0e_0_usa")

curs = db.cursor()
curs.execute("SELECT * FROM states ORDER BY states.id ASC")
res = curs.fetchall()

for i in res:
    print(i)

db.close()
