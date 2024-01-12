#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
host = "localhost"
port = 3306

if __name__ == "__main__":
    db = MySQLdb.connect(host=host, user=user,
                         passwd=password, db=database, port=port)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
