#!/usr/bin/python3

"""demo of script that lists states in database
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    # ensure correct number of arguments
    if len(argv) != 5:
        exit(1)

    # extract arguments
    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    try:

        # create connector object that will connect to database
        connector = MySQLdb.connect(
                host='localhost', 
                port=3306, 
                user=argv[1], 
                passwd=argv[2],
                db=argv[3]
                )

        # create cursor object that will interact with the database
        myCursor = connector.cursor()

        # execute the commands required
        myCursor.execute("SELECT * FROM states WHERE name=%s ORDER BY states.id", (argv[4],))

        # fetch all the results of the query
        records = myCursor.fetchall()

        # iterate through the results in order to print each item
        for record in records:
            print(f"{record}")
    
    
        connector.close()

    except MySQLdb.Error as e:
        exit(1)
