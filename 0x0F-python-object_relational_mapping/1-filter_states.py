#!/usr/bin/python3
"""Module that Get all states"""
import MySQLdb
import sys

if __name__ == "__main__":
    u_name = sys.argv[1]
    passw = sys.argv[2]
    d_base = sys.argv[3]

    mydb = MySQLdb.connect(
            host="localhost", port=3306, user=u_name, passwd=passw, db=d_base)

    curs = mydb.cursor()
    curs.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    res = curs.fetchall()

    for i in res:
        print(i)

    curs.close()
    mydb.close()
