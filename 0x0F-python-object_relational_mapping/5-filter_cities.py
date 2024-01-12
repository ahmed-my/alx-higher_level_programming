#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities INNER JOIN
                   states ON states.id=cities.state_id WHERE
                   states.name=%s""", (state_name,))
    cities = cursor.fetchall()
    cities_list = list(city[0] for city in cities)
    cities_join = ', '.join(cities_list)
    print(cities_join)
    cursor.close()
    db.close()
