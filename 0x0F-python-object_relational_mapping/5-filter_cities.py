#!/usr/bin/python3


"""demo script of displaying cities that are in a state
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':

    """make connection to database"""
    myDB = MySQLdb.connect(user=argv[1],
                        passwd=argv[2],
                        db=argv[3],
                        host='localhost',
                        port=3306
                        )

    """create variable to hold the inputed state value"""
    myState = argv[4]

    """create cursor object to interact with database"""
    myCur = myDB.cursor()

    """execute the query-refer to first comment"""
    myCur.execute("SELECT cities.name FROM cities INNER JOIN hbtn_0e_4_usa.states ON cities.state_id = states.id WHERE states.name = '{}'".format(myState))

    result = myCur.fetchall()

    for item in result:
        print(*item, sep=", ", end=", ")
    print()

    myCur.close()

    myDB.close()
