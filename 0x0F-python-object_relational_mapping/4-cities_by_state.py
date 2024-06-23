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

    myQuery = "SELECT cities.id, cities.name, states.name FROM cities JOIN hbtn_0e_0_usa.states ON cities.state_id = states.id ORDER BY cities.id"

    myCur.execute(myQuery)

    items = myCur.fetchall()

    for item in items:
        print(item)

    myCur.close()

    myDB.close()
