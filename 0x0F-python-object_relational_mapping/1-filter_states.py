#!/usr/bin/python3

"""script displaying all states with name starting with N(upper)
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    myDB = MySQLdb.connect(user=argv[1],
                        passwd=argv[2],
                        db=argv[3]
                        )

    myCur = myDB.cursor()

    myCur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

    nStates = myCur.fetchall()

    for state in nStates:
        print(state)

    myCur.close()

    myDB.close()
