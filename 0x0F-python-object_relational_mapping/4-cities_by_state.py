#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa
   Cities by states
"""
import MySQLdb
import sys


if __name__ == "__main__":
    u_name = sys.argv[1]
    passw = sys.argv[2]
    d_name = sys.argv[3]

    mydb = MySQLdb.connect(
            host="localhost", port=3306, user=u_name, passwd=passw, db=d_name)
    curs = mydb.cursor()
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               JOIN states
               ON cities.state_id = states.id
               ORDER BY cities.id"""
    curs.execute(query)
    res = curs.fetchall()

    for i in res:
        print(i)

    curs.close()
    mydb.close()
