#!/usr/bin/python3
""" A module that list all `cities` in thw database `hbth_0e_4_usa`"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cusr = db.cursor()
    cusr.execute("SELECT c.id, c.name, s.name\
                    FROM cities AS c\
                        INNER JOIN states AS s\
                             ON c.state_id = s.id")

    cities = cusr.fetchall()

    for city in cities:
        print(city)

    cusr.close()
    db.close()
