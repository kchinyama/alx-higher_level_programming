#!/usr/bin/python3

"""
demo script that displaysname of city typed to input
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    """the arguments needed for the query"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        state_name = argv[4])

    """create cursor object to navigate the database and tables"""
    mycur = db.cursor()

    """use cursor object to execute command to list all states in database"""
    mycur.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id"(state_name))

    """use loop to display results"""
    queried_items = mycur.fetchall()

    for state in queried_items:
        print(state)

    mycur.close()
    db.close()
