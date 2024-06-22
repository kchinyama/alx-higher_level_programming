#!/usr/bin/python3

"""script displaying all states
"""


import MySQLdb
import sys

if __name__ == '__main__':

    myDB = MySQLdb.connect(user=sys.argv[1], 
                        passwd=sys.argv[2],
                        db=sys.argv[3]
                        )

    myCur = myDB.cursor()

    myCur.execute("SELECT * FROM states ORDER BY states.id")

    allStates = myCur.fetchall()

    for state in allStates:
        print(state)

    myCur.close()

    myDB.close()
