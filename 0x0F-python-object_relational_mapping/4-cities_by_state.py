#!/usr/bin/python3

"""script demo of creating cities and joining to states
table
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':

    myDB = MySQLdb.connect(user=argv[1],
                        passwd=argv[2],
                        db=argv[3]
                        )

    myCur = myDB.cursor()

    myQuery = "SELECT cities.id, cities.name FROM cities ORDER BY cities.id"

    myCur.execute(myQuery)

    items = myCur.fetchall()

    for item in items:
        print(item)

    myCur.close()

    myDB.close()
