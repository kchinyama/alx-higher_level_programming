#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]


    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()


    query = "SELECT cities.id cities.name state.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)


    data = cursor.fetchall()


    for row in data:
        print(row)


    cursor.close()
    db.close()
