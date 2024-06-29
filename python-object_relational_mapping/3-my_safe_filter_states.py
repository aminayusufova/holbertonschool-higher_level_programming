#!/usr/bin/python3
"""A module safe from SQL injection /* store quaries in var*/"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cusr = db.cursor()

    query = "SELECT * FROM states WHERE name = %s"
    usr_input = sys.argv[4]
    cusr.execute(query, (usr_input,))

    states = cusr.fetchall()
    for state in states:
        print(state)
    cusr.close()
    db.close()
