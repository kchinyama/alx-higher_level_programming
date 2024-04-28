#!/usr/bin/python3

"""demo of safe injection intop data base(protected from SQL Injection
"""



import MySQLdb
from sys import argv


if __name__ == "__main__":

    try:
        # create connector object to connect to the database
        connector = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3]
                )
        # create cursor object to interact with the database
        myCursor = connector.cursor()

        # execute desired commands/queries
        query = "SELECT * FROM states WHERE name=%s ORDER BY states.id"
        myCursor.execute(query, (argv[4],))

        # fetach all results
        records = myCursor.fetchall()

        # iterate through list to get each record
        for record in records:
            print(f"{record}")

    # close the connection
    finally:
        connector.close()
