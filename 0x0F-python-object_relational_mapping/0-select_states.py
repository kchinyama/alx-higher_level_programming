#!/usr/bin/python3

"""
demo script that displays all cities in database
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    """the arguments needed for the query"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    """create cursor object to navigate the database and tables"""
    mycur = db.cursor()

    """use cursor object to execute command to list all states in database"""
    mycur.execute("SELECT * FROM states ORDER BY states.id ASC")

    """use loop to display results"""
    queried_items = mycur.fetchall()

    for state in queried_items:
        print(state)

    mycur.close()
    db.close()
