#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                   cities INNER JOIN states ON states.id=cities.state_id""")
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()
