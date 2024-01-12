#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa starting with N"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == "N":
            print(state)
    cursor.close()
    db.close()
