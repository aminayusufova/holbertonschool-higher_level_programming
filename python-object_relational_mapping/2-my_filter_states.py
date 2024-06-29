#!/usr/bin/python3
"""A module that displays the values of `state` in `db`"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cusr = db.cursor()
    cusr.execute(
        "SELECT * FROM states WHERE BINARY name = '{}'".format(sys.argv[4])
            )
    states = cusr.fetchall()
    for state in states:
        print(state)

    cusr.close()
    db.close()
