#!/usr/bin/python3

"""script demo of displaying values where name matches
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':

    myDB = MySQLdb.connect(user=argv[1],
                        passwd=argv[2],
                        db=argv[3]
                        )

    myCur = myDB.cursor()

    myState = argv[4]

    myCur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id;".format(myState))

    result = myCur.fetchall()
    
    for item in result:
        print(item)

    myCur.close()

    myDB.close()
