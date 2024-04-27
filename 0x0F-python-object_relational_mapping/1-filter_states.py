#!/usr/bin/python3

"""demop of scrit that selects records via the filter_by clause
"""



import MySQLdb
from sys import argv


if __name__ == '__main__':

    try:
        """create a conncetion object that will conncet to the databse"""

        connector = MySQLdb.connect(
                user=argv[1],
                passwd=argv[2],
                db=argv[3]
                )

        """create cursor to interact with database"""
        myCursor = connector.cursor()

        """execute the command required"""
        myCursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")

        """collect all the records"""
        records = myCursor.fetchall()

        """iterate through the records and print each record"""
        for record in records:
            print(record)

    finally:
        """close the connection"""
        connector.close()
        #myCursor.close()
