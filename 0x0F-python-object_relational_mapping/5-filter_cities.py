#!/usr/bin/python3

"""demo of script that lists states in database
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

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
    myCursor.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name=%s ORDER BY cities.id", (argv[4],))

    # fetch all the results of the query
    records = myCursor.fetchall()

    # iterate through the results in order to print each item
    for record in records:
        print(f"{record[0]}")
    
    # best practuce to close conncetio once done
    connector.close()
